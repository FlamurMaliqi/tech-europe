from dataclasses import dataclass
from typing import Annotated, Literal
from pydantic import Field
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
from livekit.agents import (
    Agent,
    AgentSession,
    FunctionTool,
    JobContext,
    RunContext,
    ToolError,
    WorkerOptions,
    cli,
    function_tool,
)
from livekit.agents import stt, llm
from typing import AsyncIterator, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from livekit.agents.types import TimedString, ModelSettings
# Note: Some LiveKit imports may not be available in all versions
# We'll implement our own metrics collection system
import logging
import asyncio
import time
from datetime import datetime
from typing import Dict, List, Optional
from livekit.plugins import openai, silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel

from drive_thru.database import (
    COMMON_INSTRUCTIONS,
    FakeDB,
    MenuItem,
    find_items_by_id,
    menu_instructions,
)
from drive_thru.order import (
    OrderedCombo, 
    OrderedHappy, 
    OrderedRegular, 
    OrderState, 
    OrderStatus,
    ConversationMetrics
)
from drive_thru.data_pipeline import data_pipeline
from drive_thru.database_config import get_database


class DriveThruMetrics:
    """Comprehensive metrics collection for drive-thru operations"""
    
    def __init__(self):
        # Initialize our custom metrics collection
        self.logger = logging.getLogger(__name__)
        
        # Real-time metrics
        self.session_metrics: Dict[str, Dict] = {}
        self.business_metrics = {
            "total_orders": 0,
            "successful_orders": 0,
            "failed_orders": 0,
            "cancelled_orders": 0,
            "total_revenue": 0.0,
            "average_order_value": 0.0,
            "average_conversation_duration": 0.0,
            "total_conversations": 0,
            "average_sentiment_score": 0.0,
            "total_tool_calls": 0,
            "successful_tool_calls": 0,
            "error_count": 0,
            "interruption_count": 0,
        }
        
        # Performance metrics
        self.performance_metrics = {
            "average_response_time": 0.0,
            "tool_call_success_rate": 0.0,
            "conversation_success_rate": 0.0,
            "customer_satisfaction_rate": 0.0,
        }
        
        # Item popularity tracking
        self.item_metrics: Dict[str, int] = {}
        self.combo_metrics: Dict[str, int] = {}
        self.drink_metrics: Dict[str, int] = {}
        
    def start_session_metrics(self, session_id: str, conversation_id: str):
        """Initialize metrics for a new session"""
        self.session_metrics[session_id] = {
            "conversation_id": conversation_id,
            "start_time": time.time(),
            "end_time": None,
            "duration": 0.0,
            "turns": 0,
            "user_turns": 0,
            "agent_turns": 0,
            "tool_calls": 0,
            "successful_tool_calls": 0,
            "errors": 0,
            "interruptions": 0,
            "order_success": False,
            "sentiment_score": 0.0,
            "customer_satisfaction": None,
            "order_value": 0.0,
            "items_ordered": [],
        }
        
    def end_session_metrics(self, session_id: str, order_state: OrderState):
        """Finalize metrics for a completed session"""
        if session_id not in self.session_metrics:
            return
            
        session = self.session_metrics[session_id]
        session["end_time"] = time.time()
        session["duration"] = session["end_time"] - session["start_time"]
        session["order_success"] = order_state.status == OrderStatus.COMPLETED
        session["order_value"] = order_state.total_price
        
        # Update business metrics
        self.business_metrics["total_conversations"] += 1
        self.business_metrics["total_orders"] += 1
        
        if session["order_success"]:
            self.business_metrics["successful_orders"] += 1
            self.business_metrics["total_revenue"] += session["order_value"]
        elif order_state.status == OrderStatus.CANCELLED:
            self.business_metrics["cancelled_orders"] += 1
        else:
            self.business_metrics["failed_orders"] += 1
            
        # Update performance metrics
        self._update_performance_metrics()
        
        # Log metrics
        self._log_session_metrics(session_id, session)
        
    def update_turn_metrics(self, session_id: str, is_user: bool = True):
        """Update turn counting metrics"""
        if session_id in self.session_metrics:
            self.session_metrics[session_id]["turns"] += 1
            if is_user:
                self.session_metrics[session_id]["user_turns"] += 1
            else:
                self.session_metrics[session_id]["agent_turns"] += 1
                
    def update_tool_call_metrics(self, session_id: str, successful: bool = True):
        """Update tool call metrics"""
        if session_id in self.session_metrics:
            self.session_metrics[session_id]["tool_calls"] += 1
            self.business_metrics["total_tool_calls"] += 1
            
            if successful:
                self.session_metrics[session_id]["successful_tool_calls"] += 1
                self.business_metrics["successful_tool_calls"] += 1
            else:
                self.session_metrics[session_id]["errors"] += 1
                self.business_metrics["error_count"] += 1
                
    def update_error_metrics(self, session_id: str):
        """Update error counting"""
        if session_id in self.session_metrics:
            self.session_metrics[session_id]["errors"] += 1
            self.business_metrics["error_count"] += 1
            
    def update_interruption_metrics(self, session_id: str):
        """Update interruption counting"""
        if session_id in self.session_metrics:
            self.session_metrics[session_id]["interruptions"] += 1
            self.business_metrics["interruption_count"] += 1
            
    def update_item_metrics(self, item_id: str, item_type: str = "regular"):
        """Track item popularity"""
        if item_type == "combo":
            self.combo_metrics[item_id] = self.combo_metrics.get(item_id, 0) + 1
        elif item_type == "drink":
            self.drink_metrics[item_id] = self.drink_metrics.get(item_id, 0) + 1
        else:
            self.item_metrics[item_id] = self.item_metrics.get(item_id, 0) + 1
            
    def update_sentiment_metrics(self, session_id: str, sentiment_score: float):
        """Update sentiment tracking"""
        if session_id in self.session_metrics:
            self.session_metrics[session_id]["sentiment_score"] = sentiment_score
            
    def _update_performance_metrics(self):
        """Calculate performance metrics from collected data"""
        if self.business_metrics["total_tool_calls"] > 0:
            self.performance_metrics["tool_call_success_rate"] = (
                self.business_metrics["successful_tool_calls"] / 
                self.business_metrics["total_tool_calls"]
            ) * 100
            
        if self.business_metrics["total_orders"] > 0:
            self.performance_metrics["conversation_success_rate"] = (
                self.business_metrics["successful_orders"] / 
                self.business_metrics["total_orders"]
            ) * 100
            
        if self.business_metrics["total_orders"] > 0:
            self.business_metrics["average_order_value"] = (
                self.business_metrics["total_revenue"] / 
                self.business_metrics["total_orders"]
            )
            
        # Calculate average conversation duration
        if self.session_metrics:
            total_duration = sum(s["duration"] for s in self.session_metrics.values() if s["duration"] > 0)
            completed_sessions = len([s for s in self.session_metrics.values() if s["duration"] > 0])
            if completed_sessions > 0:
                self.business_metrics["average_conversation_duration"] = total_duration / completed_sessions
                
    def _log_session_metrics(self, session_id: str, session: Dict):
        """Log session metrics using standard Python logging"""
        metrics_data = {
            "session_id": session_id,
            "conversation_id": session["conversation_id"],
            "duration": session["duration"],
            "turns": session["turns"],
            "tool_calls": session["tool_calls"],
            "successful_tool_calls": session["successful_tool_calls"],
            "errors": session["errors"],
            "interruptions": session["interruptions"],
            "order_success": session["order_success"],
            "order_value": session["order_value"],
            "sentiment_score": session["sentiment_score"],
        }
        
        self.logger.info(f"DRIVE_THRU_SESSION_METRICS: {metrics_data}")
        
    def get_business_summary(self) -> Dict:
        """Get comprehensive business metrics summary"""
        return {
            "business_metrics": self.business_metrics,
            "performance_metrics": self.performance_metrics,
            "popular_items": dict(sorted(self.item_metrics.items(), key=lambda x: x[1], reverse=True)[:10]),
            "popular_combos": dict(sorted(self.combo_metrics.items(), key=lambda x: x[1], reverse=True)[:5]),
            "popular_drinks": dict(sorted(self.drink_metrics.items(), key=lambda x: x[1], reverse=True)[:5]),
        }
        
    def export_metrics(self) -> Dict:
        """Export all metrics for external consumption"""
        return {
            "session_metrics": self.session_metrics,
            "business_summary": self.get_business_summary(),
            "timestamp": time.time(),
        }


@dataclass
class Userdata:
    order: OrderState
    drink_items: list[MenuItem]
    combo_items: list[MenuItem]
    happy_items: list[MenuItem]
    regular_items: list[MenuItem]
    sauce_items: list[MenuItem]
    metrics: DriveThruMetrics
    session_id: str
    feedback_requested: bool = False
    feedback_collected: bool = False
    customer_feedback: str = ""


class DriveThruAgent(Agent):
    def __init__(self, *, userdata: Userdata) -> None:
        self.userdata = userdata
        instructions = (
            COMMON_INSTRUCTIONS
            + "\n\n"
            + menu_instructions("drink", items=userdata.drink_items)
            + "\n\n"
            + menu_instructions("combo_meal", items=userdata.combo_items)
            + "\n\n"
            + menu_instructions("happy_meal", items=userdata.happy_items)
            + "\n\n"
            + menu_instructions("regular", items=userdata.regular_items)
            + "\n\n"
            + menu_instructions("sauce", items=userdata.sauce_items)
        )

        super().__init__(
            instructions=instructions,
            tools=[
                self.build_regular_order_tool(
                    userdata.regular_items, userdata.drink_items, userdata.sauce_items
                ),
                self.build_combo_order_tool(
                    userdata.combo_items, userdata.drink_items, userdata.sauce_items
                ),
                self.build_happy_order_tool(
                    userdata.happy_items, userdata.drink_items, userdata.sauce_items
                ),
                self.build_remove_order_tool(),
                self.build_list_order_tool(),
                self.build_complete_order_tool(),
                self.build_cancel_order_tool(),
                self.build_order_summary_tool(),
                self.build_metrics_tool(),
                self.build_request_feedback_tool(),
                self.build_collect_feedback_tool(),
                self.build_skip_feedback_tool(),
            ],
        )
    

    def build_combo_order_tool(
        self,
        combo_items: list[MenuItem],
        drink_items: list[MenuItem],
        sauce_items: list[MenuItem],
    ) -> FunctionTool:
        available_combo_ids = {item.id for item in combo_items}
        available_drink_ids = {item.id for item in drink_items}
        available_sauce_ids = {item.id for item in sauce_items}

        @function_tool
        async def order_combo_meal(
            ctx: RunContext[Userdata],
            meal_id: Annotated[
                str,
                Field(
                    description="The ID of the combo meal the user requested.",
                    json_schema_extra={"enum": list(available_combo_ids)},
                ),
            ],
            drink_id: Annotated[
                str,
                Field(
                    description="The ID of the drink the user requested.",
                    json_schema_extra={"enum": list(available_drink_ids)},
                ),
            ],
            drink_size: Literal["M", "L", "null"] | None,
            fries_size: Literal["M", "L"],
            sauce_id: Annotated[
                str,
                Field(
                    description="The ID of the sauce the user requested.",
                    json_schema_extra={"enum": [*available_sauce_ids, "null"]},
                ),
            ]
            | None,
        ):
            """
            Call this when the user orders a **Combo Meal**, like: “Number 4b with a large Sprite” or “I'll do a medium meal.”

            Do not call this tool unless the user clearly refers to a known combo meal by name or number.
            Regular items like a single cheeseburger cannot be made into a meal unless such a combo explicitly exists.

            Only call this function once the user has clearly specified both a drink and a sauce — always ask for them if they're missing.

            A meal can only be Medium or Large; Small is not an available option.
            Drink and fries sizes can differ (e.g., “large fries but a medium Coke”).

            If the user says just “a large meal,” assume both drink and fries are that size.
            """
            if not find_items_by_id(combo_items, meal_id):
                ctx.userdata.order.increment_tool_calls(successful=False)
                ctx.userdata.order.increment_error_count()
                ctx.userdata.metrics.update_tool_call_metrics(ctx.userdata.session_id, successful=False)
                ctx.userdata.metrics.update_error_metrics(ctx.userdata.session_id)
                raise ToolError(f"error: the meal {meal_id} was not found")

            drink_sizes = find_items_by_id(drink_items, drink_id)
            if not drink_sizes:
                ctx.userdata.order.increment_tool_calls(successful=False)
                ctx.userdata.order.increment_error_count()
                ctx.userdata.metrics.update_tool_call_metrics(ctx.userdata.session_id, successful=False)
                ctx.userdata.metrics.update_error_metrics(ctx.userdata.session_id)
                raise ToolError(f"error: the drink {drink_id} was not found")

            if drink_size == "null":
                drink_size = None

            if sauce_id == "null":
                sauce_id = None

            available_sizes = list({item.size for item in drink_sizes if item.size})
            if drink_size is None and len(available_sizes) > 1:
                raise ToolError(
                    f"error: {drink_id} comes with multiple sizes: {', '.join(available_sizes)}. "
                    "Please clarify which size should be selected."
                )

            if drink_size is not None and not available_sizes:
                raise ToolError(
                    f"error: size should not be specified for item {drink_id} as it does not support sizing options."
                )

            available_sizes = list({item.size for item in drink_sizes if item.size})
            if drink_size not in available_sizes:
                drink_size = None
                # raise ToolError(
                #     f"error: unknown size {drink_size} for {drink_id}. Available sizes: {', '.join(available_sizes)}."
                # )

            if sauce_id and not find_items_by_id(sauce_items, sauce_id):
                ctx.userdata.order.increment_tool_calls(successful=False)
                ctx.userdata.order.increment_error_count()
                ctx.userdata.metrics.update_tool_call_metrics(ctx.userdata.session_id, successful=False)
                ctx.userdata.metrics.update_error_metrics(ctx.userdata.session_id)
                raise ToolError(f"error: the sauce {sauce_id} was not found")

            item = OrderedCombo(
                meal_id=meal_id,
                drink_id=drink_id,
                drink_size=drink_size,
                sauce_id=sauce_id,
                fries_size=fries_size,
            )
            await ctx.userdata.order.add(item)
            ctx.userdata.order.increment_tool_calls(successful=True)
            
            # Update metrics
            ctx.userdata.metrics.update_tool_call_metrics(ctx.userdata.session_id, successful=True)
            ctx.userdata.metrics.update_item_metrics(meal_id, "combo")
            ctx.userdata.metrics.update_item_metrics(drink_id, "drink")
            if sauce_id:
                ctx.userdata.metrics.update_item_metrics(sauce_id, "sauce")
            
            return f"The item was added: {item.model_dump_json()}"

        return order_combo_meal

    def build_happy_order_tool(
        self,
        happy_items: list[MenuItem],
        drink_items: list[MenuItem],
        sauce_items: list[MenuItem],
    ) -> FunctionTool:
        available_happy_ids = {item.id for item in happy_items}
        available_drink_ids = {item.id for item in drink_items}
        available_sauce_ids = {item.id for item in sauce_items}

        @function_tool
        async def order_happy_meal(
            ctx: RunContext[Userdata],
            meal_id: Annotated[
                str,
                Field(
                    description="The ID of the happy meal the user requested.",
                    json_schema_extra={"enum": list(available_happy_ids)},
                ),
            ],
            drink_id: Annotated[
                str,
                Field(
                    description="The ID of the drink the user requested.",
                    json_schema_extra={"enum": list(available_drink_ids)},
                ),
            ],
            drink_size: Literal["S", "M", "L", "null"] | None,
            sauce_id: Annotated[
                str,
                Field(
                    description="The ID of the sauce the user requested.",
                    json_schema_extra={"enum": [*available_sauce_ids, "null"]},
                ),
            ]
            | None,
        ) -> str:
            """
            Call this when the user orders a **Happy Meal**, typically for children. These meals come with a main item, a drink, and a sauce.

            The user must clearly specify a valid Happy Meal option (e.g., “Can I get a Happy Meal?”).

            Before calling this tool:
            - Ensure the user has provided all required components: a valid meal, drink, drink size, and sauce.
            - If any of these are missing, prompt the user for the missing part before proceeding.

            Assume Small as default only if the user says "Happy Meal" and gives no size preference, but always ask for clarification if unsure.
            """
            if not find_items_by_id(happy_items, meal_id):
                raise ToolError(f"error: the meal {meal_id} was not found")

            drink_sizes = find_items_by_id(drink_items, drink_id)
            if not drink_sizes:
                raise ToolError(f"error: the drink {drink_id} was not found")

            if drink_size == "null":
                drink_size = None

            if sauce_id == "null":
                sauce_id = None

            available_sizes = list({item.size for item in drink_sizes if item.size})
            if drink_size is None and len(available_sizes) > 1:
                raise ToolError(
                    f"error: {drink_id} comes with multiple sizes: {', '.join(available_sizes)}. "
                    "Please clarify which size should be selected."
                )

            if drink_size is not None and not available_sizes:
                drink_size = None

            if sauce_id and not find_items_by_id(sauce_items, sauce_id):
                raise ToolError(f"error: the sauce {sauce_id} was not found")

            item = OrderedHappy(
                meal_id=meal_id,
                drink_id=drink_id,
                drink_size=drink_size,
                sauce_id=sauce_id,
            )
            await ctx.userdata.order.add(item)
            ctx.userdata.order.increment_tool_calls(successful=True)
            
            # Update metrics
            ctx.userdata.metrics.update_tool_call_metrics(ctx.userdata.session_id, successful=True)
            ctx.userdata.metrics.update_item_metrics(meal_id, "combo")  # Happy meals are tracked as combos
            ctx.userdata.metrics.update_item_metrics(drink_id, "drink")
            if sauce_id:
                ctx.userdata.metrics.update_item_metrics(sauce_id, "sauce")
            
            return f"The item was added: {item.model_dump_json()}"

        return order_happy_meal

    def build_regular_order_tool(
        self,
        regular_items: list[MenuItem],
        drink_items: list[MenuItem],
        sauce_items: list[MenuItem],
    ) -> FunctionTool:
        all_items = regular_items + drink_items + sauce_items
        available_ids = {item.id for item in all_items}

        @function_tool
        async def order_regular_item(
            ctx: RunContext[Userdata],
            item_id: Annotated[
                str,
                Field(
                    description="The ID of the item the user requested.",
                    json_schema_extra={"enum": list(available_ids)},
                ),
            ],
            size: Annotated[
                # models don't seem to understand `ItemSize | None`, adding the `null` inside the enum list as a workaround
                Literal["S", "M", "L", "null"] | None,
                Field(
                    description="Size of the item, if applicable (e.g., 'S', 'M', 'L'), otherwise 'null'. "
                ),
            ] = "null",
        ) -> str:
            """
            Call this when the user orders **a single item on its own**, not as part of a Combo Meal or Happy Meal.

            The customer must provide clear and specific input. For example, item variants such as flavor must **always** be explicitly stated.

            The user might say—for example:
            - “Just the cheeseburger, no meal”
            - “A medium Coke”
            - “Can I get some ketchup?”
            - “Can I get a McFlurry Oreo?”
            """
            item_sizes = find_items_by_id(all_items, item_id)
            if not item_sizes:
                raise ToolError(f"error: {item_id} was not found.")

            if size == "null":
                size = None

            available_sizes = list({item.size for item in item_sizes if item.size})
            if size is None and len(available_sizes) > 1:
                raise ToolError(
                    f"error: {item_id} comes with multiple sizes: {', '.join(available_sizes)}. "
                    "Please clarify which size should be selected."
                )

            if size is not None and not available_sizes:
                size = None
                # raise ToolError(
                #     f"error: size should not be specified for item {item_id} as it does not support sizing options."
                # )

            if (size and available_sizes) and size not in available_sizes:
                raise ToolError(
                    f"error: unknown size {size} for {item_id}. Available sizes: {', '.join(available_sizes)}."
                )

            item = OrderedRegular(item_id=item_id, size=size)
            await ctx.userdata.order.add(item)
            ctx.userdata.order.increment_tool_calls(successful=True)
            
            # Update metrics
            ctx.userdata.metrics.update_tool_call_metrics(ctx.userdata.session_id, successful=True)
            ctx.userdata.metrics.update_item_metrics(item_id, "regular")
            
            return f"The item was added: {item.model_dump_json()}"

        return order_regular_item

    def build_remove_order_tool(self) -> FunctionTool:
        @function_tool
        async def remove_order_item(
            ctx: RunContext[Userdata],
            order_id: Annotated[
                list[str],
                Field(
                    description="A list of internal `order_id`s of the items to remove. Use `list_order_items` to look it up if needed."
                ),
            ],
        ) -> str:
            """
            Removes one or more items from the user's order using their `order_id`s.

            Useful when the user asks to cancel or delete existing items (e.g., "Remove the cheeseburger").

            If the `order_id`s are unknown, call `list_order_items` first to retrieve them.
            """
            not_found = [oid for oid in order_id if oid not in ctx.userdata.order.items]
            if not_found:
                ctx.userdata.order.increment_tool_calls(successful=False)
                ctx.userdata.order.increment_error_count()
                ctx.userdata.metrics.update_tool_call_metrics(ctx.userdata.session_id, successful=False)
                ctx.userdata.metrics.update_error_metrics(ctx.userdata.session_id)
                raise ToolError(
                    f"error: no item(s) found with order_id(s): {', '.join(not_found)}"
                )

            removed_items = [await ctx.userdata.order.remove(oid) for oid in order_id]
            ctx.userdata.order.increment_tool_calls(successful=True)
            ctx.userdata.metrics.update_tool_call_metrics(ctx.userdata.session_id, successful=True)
            
            return "Removed items:\n" + "\n".join(
                item.model_dump_json() for item in removed_items
            )
        
        return remove_order_item

    def build_list_order_tool(self) -> FunctionTool:
        @function_tool
        async def list_order_items(ctx: RunContext[Userdata]) -> str:
            """
            Retrieves the current list of items in the user's order, including each item's internal `order_id`.

            Helpful when:
            - An `order_id` is required before modifying or removing an existing item.
            - Confirming details or contents of the current order.

            Examples:
            - User requests modifying an item, but the item's `order_id` is unknown (e.g., "Change the fries from small to large").
            - User requests removing an item, but the item's `order_id` is unknown (e.g., "Remove the cheeseburger").
            - User asks about current order details (e.g., "What's in my order so far?").
            """
            items = ctx.userdata.order.items.values()
            if not items:
                return "The order is empty"

            return "\n".join(item.model_dump_json() for item in items)
        
        return list_order_items

    def build_complete_order_tool(self) -> FunctionTool:
        @function_tool
        async def complete_order(ctx: RunContext[Userdata]) -> str:
            """
            Complete the current order and mark it as successful.
            Call this when the customer confirms they are done ordering and ready to proceed.
            """
            if not ctx.userdata.order.items:
                return "The order is empty. Please add some items before completing the order."
            
            # Mark that we're requesting feedback
            ctx.userdata.feedback_requested = True
            
            # Update total price before showing summary
            await ctx.userdata.order._update_total_price()
            
            return f"Perfect! Your order is ready. Total: ${ctx.userdata.order.total_price:.2f} for {len(ctx.userdata.order.items)} items. Would you like to provide any feedback about your experience today?"
        
        return complete_order

    def build_cancel_order_tool(self) -> FunctionTool:
        @function_tool
        async def cancel_order(ctx: RunContext[Userdata]) -> str:
            """
            Cancel the current order.
            Call this when the customer wants to cancel their entire order.
            """
            ctx.userdata.order.mark_cancelled()
            ctx.userdata.order.increment_tool_calls(successful=True)
            ctx.userdata.metrics.update_tool_call_metrics(ctx.userdata.session_id, successful=True)
            
            # Automatically save data when order is cancelled
            try:
                # Finalize metrics
                ctx.userdata.metrics.end_session_metrics(ctx.userdata.session_id, ctx.userdata.order)
                final_metrics = ctx.userdata.metrics.export_metrics()
                
                # Process through data pipeline
                pipeline_result = await data_pipeline.process_conversation_data(
                    ctx.userdata.session_id,
                    ctx.userdata.order,
                    final_metrics
                )
                
                if pipeline_result['status'] == 'success':
                    print(f"✅ Cancelled order data saved to database: {pipeline_result['conversation_id']}")
                else:
                    print(f"⚠️ Data pipeline warning: {pipeline_result['message']}")
                    
            except Exception as e:
                print(f"❌ Data pipeline error: {e}")
                # Don't fail the order cancellation if data pipeline fails
            
            return "Order has been cancelled. Thank you for visiting McDonald's!"
        
        return cancel_order

    def build_order_summary_tool(self) -> FunctionTool:
        @function_tool
        async def get_order_summary(ctx: RunContext[Userdata]) -> str:
            """
            Get a summary of the current order including status and metrics.
            """
            order = ctx.userdata.order
            summary = f"Order Status: {order.status.value}\n"
            summary += f"Total Items: {len(order.items)}\n"
            summary += f"Total Price: ${order.total_price:.2f}\n"
            summary += f"Created: {order.created_at}\n"
            summary += f"Last Updated: {order.updated_at}\n"
            
            if order.conversation_metrics:
                metrics = order.conversation_metrics
                summary += f"Conversation ID: {metrics.conversation_id}\n"
                summary += f"Duration: {metrics.duration_seconds:.1f}s\n" if metrics.duration_seconds else "Duration: Ongoing\n"
                summary += f"Total Turns: {metrics.total_turns}\n"
                summary += f"User Turns: {metrics.user_turns}\n"
                summary += f"Agent Turns: {metrics.agent_turns}\n"
                summary += f"Tool Calls: {metrics.tool_calls_count}\n"
                summary += f"Successful Tool Calls: {metrics.successful_tool_calls}\n"
                summary += f"Errors: {metrics.error_count}\n"
                summary += f"Interruptions: {metrics.interruption_count}\n"
                summary += f"Order Success: {metrics.order_success}\n"
                if metrics.sentiment:
                    summary += f"Sentiment: {metrics.sentiment.value}\n"
                if metrics.sentiment_score is not None:
                    summary += f"Sentiment Score: {metrics.sentiment_score:.2f}\n"
            
            return summary
        
        return get_order_summary

    def build_metrics_tool(self) -> FunctionTool:
        @function_tool
        async def get_real_time_metrics(ctx: RunContext[Userdata]) -> str:
            """
            Get real-time metrics and analytics for the current session and overall system.
            This provides insights into agent performance, order success rates, and business metrics.
            """
            # Get current session metrics
            session_id = ctx.userdata.session_id
            current_session = ctx.userdata.metrics.session_metrics.get(session_id, {})
            
            # Get business summary
            business_summary = ctx.userdata.metrics.get_business_summary()
            
            # Format metrics for display
            metrics_report = f"=== REAL-TIME METRICS REPORT ===\n\n"
            
            # Current Session Metrics
            metrics_report += f"📊 CURRENT SESSION ({session_id}):\n"
            metrics_report += f"  • Duration: {current_session.get('duration', 0):.1f}s\n"
            metrics_report += f"  • Turns: {current_session.get('turns', 0)} (User: {current_session.get('user_turns', 0)}, Agent: {current_session.get('agent_turns', 0)})\n"
            metrics_report += f"  • Tool Calls: {current_session.get('tool_calls', 0)} (Success: {current_session.get('successful_tool_calls', 0)})\n"
            metrics_report += f"  • Errors: {current_session.get('errors', 0)}\n"
            metrics_report += f"  • Interruptions: {current_session.get('interruptions', 0)}\n"
            metrics_report += f"  • Order Success: {current_session.get('order_success', False)}\n"
            metrics_report += f"  • Order Value: ${current_session.get('order_value', 0):.2f}\n\n"
            
            # Business Metrics
            business = business_summary["business_metrics"]
            metrics_report += f"🏪 BUSINESS METRICS:\n"
            metrics_report += f"  • Total Orders: {business['total_orders']}\n"
            metrics_report += f"  • Successful: {business['successful_orders']} ({business['successful_orders']/max(business['total_orders'], 1)*100:.1f}%)\n"
            metrics_report += f"  • Failed: {business['failed_orders']}\n"
            metrics_report += f"  • Cancelled: {business['cancelled_orders']}\n"
            metrics_report += f"  • Total Revenue: ${business['total_revenue']:.2f}\n"
            metrics_report += f"  • Avg Order Value: ${business['average_order_value']:.2f}\n"
            metrics_report += f"  • Avg Conversation Duration: {business['average_conversation_duration']:.1f}s\n\n"
            
            # Performance Metrics
            performance = business_summary["performance_metrics"]
            metrics_report += f"⚡ PERFORMANCE METRICS:\n"
            metrics_report += f"  • Tool Call Success Rate: {performance['tool_call_success_rate']:.1f}%\n"
            metrics_report += f"  • Conversation Success Rate: {performance['conversation_success_rate']:.1f}%\n"
            metrics_report += f"  • Total Tool Calls: {business['total_tool_calls']}\n"
            metrics_report += f"  • Total Errors: {business['error_count']}\n"
            metrics_report += f"  • Total Interruptions: {business['interruption_count']}\n\n"
            
            # Popular Items
            if business_summary["popular_items"]:
                metrics_report += f"🍔 POPULAR ITEMS:\n"
                for item, count in list(business_summary["popular_items"].items())[:5]:
                    metrics_report += f"  • {item}: {count} orders\n"
                metrics_report += "\n"
                
            if business_summary["popular_combos"]:
                metrics_report += f"🍟 POPULAR COMBOS:\n"
                for combo, count in list(business_summary["popular_combos"].items())[:3]:
                    metrics_report += f"  • {combo}: {count} orders\n"
                metrics_report += "\n"
                
            if business_summary["popular_drinks"]:
                metrics_report += f"🥤 POPULAR DRINKS:\n"
                for drink, count in list(business_summary["popular_drinks"].items())[:3]:
                    metrics_report += f"  • {drink}: {count} orders\n"
                    
            return metrics_report
        
        return get_real_time_metrics

    def build_request_feedback_tool(self) -> FunctionTool:
        @function_tool
        async def request_feedback(ctx: RunContext[Userdata]) -> str:
            """
            Ask the customer if they want to provide feedback.
            Call this when the customer has completed their order and you want to ask for feedback.
            """
            if not ctx.userdata.feedback_requested:
                return "Please complete the order first before requesting feedback."
            
            if ctx.userdata.feedback_collected:
                return "Feedback has already been collected for this order."
            
            return "Would you like to share any feedback about your experience today? You can tell me what you thought about the service, the ordering process, or anything else!"
        
        return request_feedback

    def build_collect_feedback_tool(self) -> FunctionTool:
        @function_tool
        async def collect_feedback(ctx: RunContext[Userdata], feedback_text: str) -> str:
            """
            Collect feedback from the customer.
            Call this when the customer provides feedback text.
            
            Args:
                feedback_text: The feedback text provided by the customer
            """
            if not ctx.userdata.feedback_requested:
                return "Please complete the order first before collecting feedback."
            
            if ctx.userdata.feedback_collected:
                return "Feedback has already been collected for this order."
            
            # Store the feedback
            ctx.userdata.customer_feedback = feedback_text
            ctx.userdata.feedback_collected = True
            
            # Also store in conversation metrics for data pipeline
            ctx.userdata.order.conversation_metrics.feedback = feedback_text
            
            # Now complete the order with feedback
            ctx.userdata.order.mark_completed()
            ctx.userdata.order.increment_tool_calls(successful=True)
            ctx.userdata.metrics.update_tool_call_metrics(ctx.userdata.session_id, successful=True)
            
            # Update total price before saving
            await ctx.userdata.order._update_total_price()
            print(f"💰 Order completed with total: ${ctx.userdata.order.total_price:.2f}")
            print(f"📝 Customer feedback: {feedback_text}")
            
            # Automatically save data when order is completed
            try:
                # Finalize metrics
                ctx.userdata.metrics.end_session_metrics(ctx.userdata.session_id, ctx.userdata.order)
                final_metrics = ctx.userdata.metrics.export_metrics()
                
                # Process through data pipeline
                pipeline_result = await data_pipeline.process_conversation_data(
                    ctx.userdata.session_id,
                    ctx.userdata.order,
                    final_metrics
                )
                
                if pipeline_result['status'] == 'success':
                    print(f"✅ Order data saved to database: {pipeline_result['conversation_id']}")
                else:
                    print(f"⚠️ Data pipeline warning: {pipeline_result['message']}")
                    
            except Exception as e:
                print(f"❌ Data pipeline error: {e}")
                # Don't fail the order completion if data pipeline fails
            
            return f"Thank you for your feedback! Your order is now complete. Order ID: {ctx.userdata.order.conversation_metrics.conversation_id}"
        
        return collect_feedback

    def build_skip_feedback_tool(self) -> FunctionTool:
        @function_tool
        async def skip_feedback(ctx: RunContext[Userdata]) -> str:
            """
            Skip feedback collection and complete the order.
            Call this when the customer declines to provide feedback.
            """
            if not ctx.userdata.feedback_requested:
                return "Please complete the order first before skipping feedback."
            
            if ctx.userdata.feedback_collected:
                return "Feedback has already been collected for this order."
            
            # Mark feedback as collected (but empty)
            ctx.userdata.feedback_collected = True
            
            # Set feedback as None in conversation metrics to indicate no feedback provided
            ctx.userdata.order.conversation_metrics.feedback = None
            
            # Now complete the order without feedback
            ctx.userdata.order.mark_completed()
            ctx.userdata.order.increment_tool_calls(successful=True)
            ctx.userdata.metrics.update_tool_call_metrics(ctx.userdata.session_id, successful=True)
            
            # Update total price before saving
            await ctx.userdata.order._update_total_price()
            print(f"💰 Order completed with total: ${ctx.userdata.order.total_price:.2f}")
            print("📝 No feedback provided by customer")
            
            # Automatically save data when order is completed
            try:
                # Finalize metrics
                ctx.userdata.metrics.end_session_metrics(ctx.userdata.session_id, ctx.userdata.order)
                final_metrics = ctx.userdata.metrics.export_metrics()
                
                # Process through data pipeline
                pipeline_result = await data_pipeline.process_conversation_data(
                    ctx.userdata.session_id,
                    ctx.userdata.order,
                    final_metrics
                )
                
                if pipeline_result['status'] == 'success':
                    print(f"✅ Order data saved to database: {pipeline_result['conversation_id']}")
                else:
                    print(f"⚠️ Data pipeline warning: {pipeline_result['message']}")
                    
            except Exception as e:
                print(f"❌ Data pipeline error: {e}")
                # Don't fail the order completion if data pipeline fails
            
            return f"Thank you! Your order is now complete. Order ID: {ctx.userdata.order.conversation_metrics.conversation_id}"
        
        return skip_feedback

    async def stt_node(
        self, audio_input: AsyncIterator, model_settings: "ModelSettings"
    ) -> AsyncIterator:
        """Override STT node to capture user speech transcripts"""
        async for ev in super().stt_node(audio_input, model_settings):
            # Capture user speech when we get final transcripts
            if hasattr(ev, 'type') and ev.type == stt.SpeechEventType.FINAL_TRANSCRIPT:
                if hasattr(ev, 'alternatives') and ev.alternatives:
                    user_text = ev.alternatives[0].text.strip()
                    if user_text:
                        self.userdata.order.add_transcript_segment(user_text, is_user=True)
                        print(f"👤 User: {user_text}")
            yield ev

    async def transcription_node(
        self, text: AsyncIterator[Union[str, "TimedString"]], model_settings: "ModelSettings"
    ) -> AsyncIterator[Union[str, "TimedString"]]:
        """Capture TTS-aligned transcriptions with timing information"""
        async for chunk in text:
            try:
                if hasattr(chunk, 'start_time') and hasattr(chunk, 'end_time'):
                    # Check if timing values are actual numbers, not NotGiven
                    start_time = getattr(chunk, 'start_time', None)
                    end_time = getattr(chunk, 'end_time', None)
                    
                    if start_time is not None and end_time is not None and start_time != "NotGiven" and end_time != "NotGiven":
                        # This is a TimedString with valid timing information
                        print(f"TimedString: '{chunk}' ({start_time:.2f}s - {end_time:.2f}s)")
                        # Add to transcript with timing info
                        self.userdata.order.add_transcript_segment(str(chunk), is_user=False)
                    else:
                        # TimedString but no valid timing
                        print(f"TimedString (no timing): '{chunk}'")
                        self.userdata.order.add_transcript_segment(str(chunk), is_user=False)
                else:
                    # Regular string
                    print(f"Regular text: '{chunk}'")
                    # Add to transcript
                    self.userdata.order.add_transcript_segment(str(chunk), is_user=False)
            except Exception as e:
                # Fallback for any formatting errors
                print(f"Text chunk: '{chunk}' (error: {e})")
                self.userdata.order.add_transcript_segment(str(chunk), is_user=False)
            
            yield chunk


async def new_userdata() -> Userdata:
    fake_db = FakeDB()
    drink_items = await fake_db.list_drinks()
    combo_items = await fake_db.list_combo_meals()
    happy_items = await fake_db.list_happy_meals()
    regular_items = await fake_db.list_regulars()
    sauce_items = await fake_db.list_sauces()

    # Initialize OrderState with empty items dict - the __post_init__ will handle the rest
    order_state = OrderState(items={})
    
    # Initialize metrics and session
    metrics = DriveThruMetrics()
    session_id = f"session_{int(time.time())}_{id(order_state)}"
    
    # Start session metrics
    metrics.start_session_metrics(session_id, order_state.conversation_metrics.conversation_id)
    
    userdata = Userdata(
        order=order_state,
        drink_items=drink_items,
        combo_items=combo_items,
        happy_items=happy_items,
        regular_items=regular_items,
        sauce_items=sauce_items,
        metrics=metrics,
        session_id=session_id,
    )
    return userdata


async def entrypoint(ctx: JobContext):
    await ctx.connect()

    userdata = await new_userdata()
    session = AgentSession[Userdata](
        userdata=userdata,
        llm=openai.LLM(
            model="gpt-4o",
            temperature=0.7,
        ),
        tts=openai.TTS(
            model="tts-1",
            voice="alloy",
        ),
        stt=openai.STT(
            model="whisper-1",
        ),
        turn_detection=MultilingualModel(),
        vad=silero.VAD.load(),
        max_tool_steps=10,
        use_tts_aligned_transcript=True,  # Enable TTS-aligned transcriptions
    )

    # Conversation capture is now handled by overriding stt_node and transcription_node methods
    
    print(f"Session started: {userdata.session_id}")
    print(f"Conversation ID: {userdata.order.conversation_metrics.conversation_id}")

    async def my_shutdown_callback(reason: str) -> None:
        print(f"Shutting agent down... Reason: {reason}")
        print(f"Final order: {session.userdata.order}")
        
        # Calculate final duration for the conversation
        if userdata.order.conversation_metrics:
            userdata.order.conversation_metrics.end_time = datetime.utcnow()
            if userdata.order.conversation_metrics.start_time:
                duration = userdata.order.conversation_metrics.end_time - userdata.order.conversation_metrics.start_time
                userdata.order.conversation_metrics.duration_seconds = duration.total_seconds()
                print(f"📊 Conversation duration: {userdata.order.conversation_metrics.duration_seconds:.2f} seconds")
        
        # Update total price before saving
        await userdata.order._update_total_price()
        print(f"💰 Final order total: ${userdata.order.total_price:.2f}")
        
        # Check if data was already saved (when order was completed/cancelled)
        if userdata.order.status in [OrderStatus.COMPLETED, OrderStatus.CANCELLED]:
            print("✅ Order data already saved automatically when order was completed/cancelled")
        else:
            print("⚠️ Order was not completed - saving partial data...")
            # Only save if order wasn't completed/cancelled
            try:
                # Finalize metrics
                userdata.metrics.end_session_metrics(userdata.session_id, userdata.order)
                
                # Export final metrics
                final_metrics = userdata.metrics.export_metrics()
                print(f"Final metrics: {final_metrics}")
                
                # Process data through pipeline
                pipeline_result = await data_pipeline.process_conversation_data(
                    userdata.session_id,
                    userdata.order,
                    final_metrics
                )
                print(f"Data pipeline result: {pipeline_result}")
            except Exception as e:
                print(f"Data pipeline error: {e}")
                # Don't fail the shutdown if data pipeline fails
        
        # Print business summary
        summary = userdata.metrics.get_business_summary()
        print(f"Business Summary: {summary}")

    ctx.add_shutdown_callback(my_shutdown_callback)

    await session.start(agent=DriveThruAgent(userdata=userdata), room=ctx.room)


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
