"""
Conversation analysis utilities for drive-thru agent
"""
import re
import json
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
from dataclasses import dataclass


@dataclass
class ConversationTurn:
    """Represents a single turn in the conversation"""
    speaker: str  # 'user' or 'agent'
    text: str
    timestamp: datetime
    turn_number: int


class ConversationAnalyzer:
    """Analyzes conversations to extract summaries, sentiment, and transcripts"""
    
    def __init__(self):
        self.sentiment_keywords = {
            'positive': [
                'great', 'excellent', 'wonderful', 'amazing', 'fantastic', 'perfect',
                'love', 'like', 'good', 'nice', 'happy', 'pleased', 'satisfied',
                'thank you', 'thanks', 'appreciate', 'wonderful', 'delicious'
            ],
            'negative': [
                'bad', 'terrible', 'awful', 'horrible', 'disgusting', 'hate',
                'angry', 'mad', 'frustrated', 'annoyed', 'disappointed', 'upset',
                'wrong', 'incorrect', 'mistake', 'problem', 'issue', 'complaint'
            ],
            'neutral': [
                'okay', 'fine', 'alright', 'sure', 'yes', 'no', 'maybe', 'perhaps'
            ]
        }
    
    def analyze_sentiment(self, text: str) -> Tuple[float, str]:
        """
        Analyze sentiment of text using AI
        Returns: (score, sentiment_type)
        score: -1.0 (very negative) to 1.0 (very positive)
        sentiment_type: 'positive', 'negative', 'neutral'
        """
        if not text:
            return 0.0, 'neutral'
        
        # For now, fall back to keyword-based approach
        # TODO: Implement AI-based sentiment analysis
        return self._analyze_sentiment_keywords(text)
    
    def _analyze_sentiment_keywords(self, text: str) -> Tuple[float, str]:
        """Fallback keyword-based sentiment analysis"""
        text_lower = text.lower()
        positive_count = 0
        negative_count = 0
        
        # Count positive and negative keywords
        for word in self.sentiment_keywords['positive']:
            positive_count += text_lower.count(word)
        
        for word in self.sentiment_keywords['negative']:
            negative_count += text_lower.count(word)
        
        # Calculate sentiment score
        total_words = len(text.split())
        if total_words == 0:
            return 0.0, 'neutral'
        
        positive_ratio = positive_count / total_words
        negative_ratio = negative_count / total_words
        
        # Calculate score (-1.0 to 1.0)
        score = positive_ratio - negative_ratio
        
        # Determine sentiment type
        if score > 0.1:
            sentiment_type = 'positive'
        elif score < -0.1:
            sentiment_type = 'negative'
        else:
            sentiment_type = 'neutral'
        
        return score, sentiment_type
    
    async def analyze_sentiment_with_ai(self, text: str, llm_client=None) -> Tuple[float, str]:
        """
        Analyze sentiment using AI/LLM for more accurate results
        Returns: (score, sentiment_type)
        score: -1.0 (very negative) to 1.0 (very positive)
        sentiment_type: 'positive', 'negative', 'neutral'
        """
        if not text or not llm_client:
            return self._analyze_sentiment_keywords(text)
        
        try:
            # Create a prompt for sentiment analysis
            prompt = f"""
Analyze the sentiment of this customer text from a drive-thru conversation:

Text: "{text}"

Please analyze the customer's emotional state and satisfaction level. Consider:
- Tone of voice indicators
- Politeness level
- Frustration or satisfaction
- Overall mood

Respond with a JSON object containing:
- "score": a number from -1.0 (very negative) to 1.0 (very positive)
- "sentiment": one of "positive", "negative", or "neutral"
- "reasoning": brief explanation of your analysis

Example response:
{{"score": 0.7, "sentiment": "positive", "reasoning": "Customer used polite language and expressed satisfaction"}}
"""

            # Call the OpenAI API with correct method
            response = await llm_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                temperature=0.3
            )
            
            # Parse the response
            response_text = response.choices[0].message.content.strip()
            
            # Try to extract JSON from the response
            if "```json" in response_text:
                json_start = response_text.find("```json") + 7
                json_end = response_text.find("```", json_start)
                json_text = response_text[json_start:json_end].strip()
            elif "{" in response_text and "}" in response_text:
                json_start = response_text.find("{")
                json_end = response_text.rfind("}") + 1
                json_text = response_text[json_start:json_end]
            else:
                # Fallback to keyword analysis
                return self._analyze_sentiment_keywords(text)
            
            # Parse JSON
            result = json.loads(json_text)
            
            score = float(result.get("score", 0.0))
            sentiment = result.get("sentiment", "neutral")
            
            # Validate score range
            score = max(-1.0, min(1.0, score))
            
            # Validate sentiment
            if sentiment not in ["positive", "negative", "neutral"]:
                sentiment = "neutral"
            
            return score, sentiment
            
        except Exception as e:
            print(f"AI sentiment analysis failed: {e}")
            # Fallback to keyword-based analysis
            return self._analyze_sentiment_keywords(text)
    
    def generate_summary(self, turns: List[ConversationTurn], order_items: List[Dict]) -> str:
        """
        Generate a conversation summary
        """
        if not turns:
            return "No conversation data available"
        
        # Extract key information
        user_turns = [t for t in turns if t.speaker == 'user']
        agent_turns = [t for t in turns if t.speaker == 'agent']
        
        # Count items ordered
        item_count = len(order_items)
        if item_count == 0:
            return "Customer inquired but did not place an order"
        
        # Get first and last user messages
        first_user_msg = user_turns[0].text if user_turns else "N/A"
        last_user_msg = user_turns[-1].text if user_turns else "N/A"
        
        # Generate summary
        summary_parts = []
        
        # Opening
        summary_parts.append(f"Customer started conversation: '{first_user_msg[:50]}...'")
        
        # Order details
        if item_count == 1:
            item_name = order_items[0].get('item_name', 'item')
            summary_parts.append(f"Ordered 1 {item_name}")
        else:
            summary_parts.append(f"Ordered {item_count} items")
        
        # Conversation flow
        if len(turns) <= 4:
            summary_parts.append("Quick, efficient conversation")
        elif len(turns) <= 8:
            summary_parts.append("Standard conversation length")
        else:
            summary_parts.append("Extended conversation with multiple interactions")
        
        # Closing
        if last_user_msg:
            summary_parts.append(f"Conversation ended with: '{last_user_msg[:30]}...'")
        
        # Add sentiment if available
        sentiment_scores = []
        for turn in user_turns:
            score, _ = self.analyze_sentiment(turn.text)
            sentiment_scores.append(score)
        
        if sentiment_scores:
            avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)
            if avg_sentiment > 0.2:
                summary_parts.append("Customer showed positive sentiment")
            elif avg_sentiment < -0.2:
                summary_parts.append("Customer showed negative sentiment")
            else:
                summary_parts.append("Customer showed neutral sentiment")
        
        return " | ".join(summary_parts)
    
    def extract_transcript(self, turns: List[ConversationTurn]) -> List[Dict]:
        """
        Extract transcript data for database storage
        """
        transcript_data = []
        for turn in turns:
            transcript_data.append({
                'speaker': turn.speaker,
                'text': turn.text,
                'timestamp': turn.timestamp,
                'turn_number': turn.turn_number
            })
        return transcript_data
    
    def analyze_conversation_quality(self, turns: List[ConversationTurn], 
                                   tool_calls: int, errors: int) -> Dict[str, Any]:
        """
        Analyze overall conversation quality
        """
        user_turns = [t for t in turns if t.speaker == 'user']
        agent_turns = [t for t in turns if t.speaker == 'agent']
        
        # Calculate metrics
        total_turns = len(turns)
        conversation_length = len(' '.join([t.text for t in turns]))
        
        # Sentiment analysis
        sentiment_scores = []
        for turn in user_turns:
            score, _ = self.analyze_sentiment(turn.text)
            sentiment_scores.append(score)
        
        avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0.0
        
        # Quality indicators
        quality_indicators = []
        
        if errors == 0:
            quality_indicators.append("error_free")
        if tool_calls > 0:
            quality_indicators.append("tool_usage")
        if total_turns <= 6:
            quality_indicators.append("efficient")
        if avg_sentiment > 0.1:
            quality_indicators.append("positive_sentiment")
        
        return {
            'total_turns': total_turns,
            'user_turns': len(user_turns),
            'agent_turns': len(agent_turns),
            'conversation_length': conversation_length,
            'average_sentiment': avg_sentiment,
            'quality_indicators': quality_indicators,
            'efficiency_score': min(1.0, 6.0 / max(total_turns, 1)),  # Higher score for fewer turns
            'sentiment_score': avg_sentiment
        }
    
    async def analyze_conversation_quality_with_ai(self, turns: List[ConversationTurn], 
                                                 tool_calls: int, errors: int, llm_client=None) -> Dict[str, Any]:
        """
        Analyze overall conversation quality using AI for sentiment analysis
        """
        user_turns = [t for t in turns if t.speaker == 'user']
        agent_turns = [t for t in turns if t.speaker == 'agent']
        
        # Calculate metrics
        total_turns = len(turns)
        conversation_length = len(' '.join([t.text for t in turns]))
        
        # Sentiment analysis using AI
        sentiment_scores = []
        if user_turns and llm_client:
            try:
                # Combine all user text for analysis
                user_text = ' '.join([turn.text for turn in user_turns])
                score, _ = await self.analyze_sentiment_with_ai(user_text, llm_client)
                sentiment_scores.append(score)
            except Exception as e:
                print(f"AI sentiment analysis failed in quality analysis: {e}")
                # Fallback to keyword analysis
                for turn in user_turns:
                    score, _ = self.analyze_sentiment(turn.text)
                    sentiment_scores.append(score)
        else:
            # Fallback to keyword analysis
            for turn in user_turns:
                score, _ = self.analyze_sentiment(turn.text)
                sentiment_scores.append(score)
        
        avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0.0
        
        # Quality indicators
        quality_indicators = []
        
        if errors == 0:
            quality_indicators.append("error_free")
        if tool_calls > 0:
            quality_indicators.append("tool_usage")
        if total_turns <= 6:
            quality_indicators.append("efficient")
        if avg_sentiment > 0.1:
            quality_indicators.append("positive_sentiment")
        
        return {
            'total_turns': total_turns,
            'user_turns': len(user_turns),
            'agent_turns': len(agent_turns),
            'conversation_length': conversation_length,
            'average_sentiment': avg_sentiment,
            'quality_indicators': quality_indicators,
            'efficiency_score': min(1.0, 6.0 / max(total_turns, 1)),  # Higher score for fewer turns
            'sentiment_score': avg_sentiment
        }


# Global analyzer instance
conversation_analyzer = ConversationAnalyzer()
