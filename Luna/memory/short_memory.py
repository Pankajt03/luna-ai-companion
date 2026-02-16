# memory/short_memory.py
from typing import List, Dict
from config.settings import MAX_SHORT_MEMORY

class ShortMemory:
    """Manages current conversation context"""
    
    def __init__(self):
        self.messages: List[Dict[str, str]] = []
    
    def add_message(self, role: str, content: str):
        """
        Add a message to short-term memory
        
        Args:
            role: 'user' or 'assistant'
            content: Message content
        """
        self.messages.append({
            "role": role,
            "content": content
        })
        
        # Keep only recent messages to avoid context overflow
        if len(self.messages) > MAX_SHORT_MEMORY:
            self.messages = self.messages[-MAX_SHORT_MEMORY:]
    
    def get_messages(self) -> List[Dict[str, str]]:
        """Get all messages in current context"""
        return self.messages.copy()
    
    def clear(self):
        """Clear short-term memory"""
        self.messages = []
    
    def get_last_message(self) -> Dict[str, str]:
        """Get the last message"""
        return self.messages[-1] if self.messages else None