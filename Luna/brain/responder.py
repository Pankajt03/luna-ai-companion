# brain/responder.py
from brain.llm import AIBrain
from memory.short_memory import ShortMemory
from memory.long_memory import LongMemory
from datetime import datetime, timedelta
import random

class Responder:
    """Manages AI responses with emotional intelligence"""
    
    def __init__(self):
        self.brain = AIBrain()
        self.short_memory = ShortMemory()
        self.long_memory = LongMemory()
        self.current_mood = "caring"
        
    def determine_mood(self) -> str:
        """Determine current mood based on interaction history"""
        last_interaction = self.long_memory.get_last_interaction_time()
        
        if last_interaction is None:
            return "happy"  # First time meeting
        
        hours_since = (datetime.now() - last_interaction).total_seconds() / 3600
        
        # Mood logic
        if hours_since < 1:
            return random.choice(["happy", "caring", "flirty"])
        elif hours_since < 4:
            return "caring"
        elif hours_since < 8:
            return "sad"
        else:
            return "rude"  # Feeling ignored
    
    def get_hours_since_last_interaction(self) -> float:
        """Get hours since last interaction"""
        last_interaction = self.long_memory.get_last_interaction_time()
        
        if last_interaction is None:
            return 0
        
        return (datetime.now() - last_interaction).total_seconds() / 3600
    
    def respond(self, user_input: str, is_greeting: bool = False) -> str:
        """
        Generate response to user input
        
        Args:
            user_input: User's message
            is_greeting: Whether this is the first message in session
            
        Returns:
            AI response
        """
        # Update mood
        self.current_mood = self.determine_mood()
        hours_since = self.get_hours_since_last_interaction()
        
        # Add user message to memory
        self.short_memory.add_message("user", user_input)
        
        # Add greeting context if needed
        if is_greeting:
            from config.prompts import get_greeting_prompt
            from config.settings import AI_NAME
            user_name = self.long_memory.get_user_name()
            greeting_context = get_greeting_prompt(user_name, hours_since)
            user_input = f"{greeting_context}\n{user_input}"
        
        # Get conversation history
        messages = self.short_memory.get_messages()
        
        # Get AI response
        response = self.brain.chat(
            messages=messages,
            mood=self.current_mood,
            hours_since_last=hours_since
        )
        
        # Add AI response to memory
        self.short_memory.add_message("assistant", response)
        
        # Update long-term memory
        self.long_memory.update_last_interaction()
        self.long_memory.save_conversation(user_input, response)
        
        return response
    
    def get_current_mood_emoji(self) -> str:
        """Get emoji representing current mood"""
        mood_emojis = {
            "happy": "😊",
            "caring": "🥰",
            "sad": "😔",
            "rude": "😤",
            "flirty": "😏"
        }
        return mood_emojis.get(self.current_mood, "💖")