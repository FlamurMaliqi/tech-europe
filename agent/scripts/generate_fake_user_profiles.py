#!/usr/bin/env python3
"""
Generate fake user profiles and store them in the Kontext vector database.
These profiles will be used by the drive-thru agent for personalized experiences.
"""

import asyncio
import json
import subprocess
from pathlib import Path
from datetime import datetime, timedelta
import random

# Path to the Kontext MCP directory (now in tech-europe workspace)
# Calculate relative path from this file to MCPs/kontext
current_file = Path(__file__)
# Go up from agent/scripts -> agent -> root -> MCPs/kontext
MCP_PATH = (current_file.parent.parent.parent / "MCPs" / "kontext").resolve()

# Sample data for generating realistic profiles
FIRST_NAMES = [
    "Alex", "Jordan", "Casey", "Morgan", "Taylor", "Riley", "Quinn",
    "Sage", "Rowan", "Dakota", "Phoenix", "River", "Skyler", "Blake",
    "Jamie", "Avery", "Cameron", "Drew", "Emery", "Finley"
]

LAST_NAMES = [
    "Anderson", "Martinez", "Johnson", "Williams", "Brown", "Davis",
    "Garcia", "Miller", "Wilson", "Moore", "Taylor", "Thomas", "Lee",
    "Jackson", "White", "Harris", "Martin", "Thompson", "Young", "King"
]

DIETARY_PREFERENCES = [
    "none", "vegetarian", "vegan", "gluten-free", "dairy-free",
    "keto", "paleo", "halal", "kosher"
]

DEFAULT_DRINKS = [
    "Coca-Cola", "Diet Coke", "Sprite", "Orange Juice", "Apple Juice",
    "Water", "Coffee", "Tea", "Iced Tea", "Lemonade"
]

MENU_ITEMS = [
    "Big Mac", "Quarter Pounder", "McChicken", "Cheeseburger", "Filet-O-Fish",
    "McDouble", "McNuggets", "McFlurry", "Fries", "Apple Pie", "Salad",
    "Wrap", "Chicken Sandwich", "Veggie Burger", "Happy Meal"
]


def generate_fake_profile(profile_id: int) -> dict:
    """Generate a realistic fake user profile"""
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    user_id = str(profile_id)
    
    # Generate dietary preferences (weighted towards common preferences)
    dietary_weights = {
        "none": 0.4,
        "vegetarian": 0.25,
        "vegan": 0.1,
        "gluten-free": 0.1,
        "dairy-free": 0.05,
        "keto": 0.05,
        "halal": 0.03,
        "kosher": 0.02
    }
    dietary = random.choices(
        list(dietary_weights.keys()),
        weights=list(dietary_weights.values())
    )[0]
    
    # Generate order history (past 3-10 orders)
    num_orders = random.randint(3, 10)
    order_history = []
    start_date = datetime.now() - timedelta(days=random.randint(30, 180))
    
    for i in range(num_orders):
        order_date = start_date + timedelta(days=i * random.randint(5, 20))
        items = random.sample(MENU_ITEMS, k=random.randint(1, 4))
        total_amount = round(random.uniform(8.00, 35.00), 2)
        
        order_history.append({
            "order_id": f"ORD-{profile_id}-{i+1:03d}",
            "date": order_date.isoformat(),
            "items": items,
            "total_amount": total_amount,
            "status": random.choice(["completed", "completed", "completed", "cancelled"])
        })
    
    # Generate personal coupons (20% chance of having active coupons)
    coupons = []
    if random.random() < 0.3:
        num_coupons = random.randint(1, 3)
        for i in range(num_coupons):
            coupon_types = [
                {"name": "Free Medium Fries", "code": f"FREEFRIES{profile_id}", "type": "free_item", "item": "Fries"},
                {"name": "20% Off Order", "code": f"SAVE20P{profile_id}", "type": "percentage", "discount": 20},
                {"name": "Buy 1 Get 1 Burger", "code": f"BOGO{profile_id}", "type": "bogo"},
                {"name": "Free Drink", "code": f"FREEDRINK{profile_id}", "type": "free_item", "item": "Drink"},
                {"name": "$5 Off $30+ Order", "code": f"SAVE5{profile_id}", "type": "dollar", "amount": 5}
            ]
            coupon = random.choice(coupon_types)
            
            # Calculate expiration date
            if order_history:
                last_order_date = datetime.fromisoformat(order_history[-1]["date"])
            else:
                last_order_date = datetime.now()
            expiration = last_order_date + timedelta(days=random.randint(30, 90))
            
            coupons.append({
                **coupon,
                "status": "active",
                "expiration": expiration.isoformat(),
                "description": f"Valid until {expiration.strftime('%Y-%m-%d')}"
            })
    
    # Calculate visit count
    visit_count = len(order_history)
    
    # Generate favorite items based on order history
    all_ordered_items = [item for order in order_history for item in order["items"]]
    item_counts = {}
    for item in all_ordered_items:
        item_counts[item] = item_counts.get(item, 0) + 1
    
    favorite_items = sorted(item_counts.items(), key=lambda x: x[1], reverse=True)[:3]
    favorite_items_list = [item[0] for item in favorite_items]
    
    # Select default drink
    default_drink = random.choice(DEFAULT_DRINKS)
    
    # Avoid items if dietary preference is vegetarian or vegan
    avoid_items = []
    if dietary in ["vegetarian", "vegan"]:
        avoid_items = ["McChicken", "Quarter Pounder", "Big Mac", "McNuggets"]
    elif dietary == "gluten-free":
        avoid_items = ["Big Mac", "Quarter Pounder"]
    elif dietary == "dairy-free":
        avoid_items = ["Cheeseburger", "McFlurry", "Apple Pie"]
    
    profile = {
        "user_id": user_id,
        "name": f"{first_name} {last_name}",
        "first_name": first_name,
        "last_name": last_name,
        "email": f"{first_name.lower()}.{last_name.lower()}@example.com",
        "phone": f"+1-555-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
        "member_since": (datetime.now() - timedelta(days=random.randint(30, 365))).isoformat(),
        "visit_count": visit_count,
        "preferences": {
            "dietary": [dietary] if dietary != "none" else [],
            "favorite_items": favorite_items_list,
            "default_drink": default_drink,
            "avoid_items": avoid_items,
            "spice_level": random.choice(["none", "mild", "medium", "hot"]),
            "size_preference": random.choice(["medium", "large", "no_preference"])
        },
        "order_history": order_history,
        "coupons": coupons,
        "metadata": {
            "profile_type": "customer",
            "created_at": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat()
        }
    }
    
    return profile


async def store_profile_in_kontext(user_id: str, profile_data: dict) -> bool:
    """Store a user profile in the Kontext vector database"""
    try:
        profile_json = json.dumps(profile_data).replace('"', '\\"')
        cmd = f"cd '{MCP_PATH}' && node -e \"import {{ KontextMCPAgent }} from './src/agent.js'; (async () => {{ const agent = new KontextMCPAgent(); await agent.initialize(); try {{ await agent.storeMemory('user_profile_{user_id}', '{profile_json}'); console.log(JSON.stringify({{success: true}})); }} catch (error) {{ console.log(JSON.stringify({{error: error.message}})); }} finally {{ await agent.terminate(); }} }})();\""
        
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=MCP_PATH)
        
        if result.returncode == 0 and 'success' in result.stdout:
            return True
        else:
            print(f"Failed to store profile for user {user_id}: {result.stdout}")
            return False
            
    except Exception as e:
        print(f"Error storing profile for user {user_id}: {e}")
        return False


async def retrieve_profile_from_kontext(user_id: str) -> dict | None:
    """Retrieve a user profile from the Kontext vector database"""
    try:
        cmd = f"cd '{MCP_PATH}' && node -e \"import {{ KontextMCPAgent }} from './src/agent.js'; (async () => {{ const agent = new KontextMCPAgent(); await agent.initialize(); try {{ const profile = await agent.retrieveMemory('user_profile_{user_id}'); if (profile && typeof profile === 'object') {{ console.log(JSON.stringify(profile)); }} else if (profile && typeof profile === 'string') {{ try {{ const parsed = JSON.parse(profile); console.log(JSON.stringify(parsed)); }} catch (e) {{ console.log(JSON.stringify({{error: 'Invalid JSON format'}})); }} }} else {{ console.log(JSON.stringify({{error: 'No profile found'}})); }} }} catch (error) {{ console.log(JSON.stringify({{error: error.message}})); }} finally {{ await agent.terminate(); }} }})();\""
        
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=MCP_PATH)
        
        if result.returncode == 0 and result.stdout.strip():
            lines = result.stdout.strip().split('\n')
            for line in reversed(lines):
                line = line.strip()
                if line.startswith('{') or line.startswith('['):
                    try:
                        data = json.loads(line)
                        if isinstance(data, dict) and not data.get('error'):
                            return data
                    except json.JSONDecodeError:
                        continue
            
            return None
        return None
        
    except Exception as e:
        print(f"Error retrieving profile for user {user_id}: {e}")
        return None


async def main():
    """Generate and store fake user profiles"""
    print("🎭 Generating fake user profiles...")
    print(f"📁 Storing profiles in Kontext vector database at: {MCP_PATH}")
    print()
    
    # Generate 20 fake user profiles
    num_profiles = 20
    generated_profiles = []
    
    for profile_id in range(1, num_profiles + 1):
        profile = generate_fake_profile(profile_id)
        generated_profiles.append(profile)
        print(f"✅ Generated profile for {profile['name']} (ID: {profile['user_id']})")
        print(f"   - Dietary: {profile['preferences']['dietary']}")
        print(f"   - Visit count: {profile['visit_count']}")
        print(f"   - Orders: {len(profile['order_history'])}")
        print(f"   - Coupons: {len(profile['coupons'])}")
        print()
    
    print("\n💾 Storing profiles in Kontext vector database...")
    print()
    
    success_count = 0
    for profile in generated_profiles:
        success = await store_profile_in_kontext(profile['user_id'], profile)
        if success:
            success_count += 1
            print(f"✅ Stored profile for {profile['name']} (ID: {profile['user_id']})")
        else:
            print(f"❌ Failed to store profile for {profile['name']} (ID: {profile['user_id']})")
    
    print()
    print(f"📊 Summary: Generated {num_profiles} profiles, successfully stored {success_count}")
    
    # Verify by retrieving a sample profile
    if success_count > 0:
        print("\n🔍 Verifying storage by retrieving a sample profile...")
        sample_profile = generated_profiles[0]
        retrieved = await retrieve_profile_from_kontext(sample_profile['user_id'])
        
        if retrieved:
            print(f"✅ Successfully retrieved profile for {retrieved.get('name', 'Unknown')}")
            print(f"   - User ID: {retrieved.get('user_id')}")
            print(f"   - Preferences: {retrieved.get('preferences', {})}")
        else:
            print("⚠️ Could not retrieve sample profile")
    
    print("\n✅ Done! User profiles are now available for the drive-thru agent.")
    print("\n📝 Sample user IDs to test with the agent:")
    for i in range(min(5, len(generated_profiles))):
        profile = generated_profiles[i]
        print(f"   - {profile['name']}: ID {profile['user_id']} (Dietary: {profile['preferences']['dietary'][0] if profile['preferences']['dietary'] else 'none'})")


if __name__ == "__main__":
    asyncio.run(main())

