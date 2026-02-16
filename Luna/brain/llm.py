# brain/llm.py
import ollama
import subprocess
from config.settings import MODEL_NAME, OLLAMA_HOST
from config.prompts import SYSTEM_PROMPT, get_mood_context
from typing import List, Dict

class AIBrain:
    """Handles communication with Ollama LLM"""
    
    def __init__(self):
        self.model = MODEL_NAME
        self.client = ollama.Client(host=OLLAMA_HOST)
        
    def chat(self, messages: List[Dict[str, str]], mood: str = "caring", hours_since_last: float = 0) -> str:
        """
        Send messages to AI and get response
        
        Args:
            messages: List of conversation messages
            mood: Current emotional state
            hours_since_last: Hours since last interaction
            
        Returns:
            AI response as string
        """
        try:
            # Add mood context to system prompt
            mood_context = get_mood_context(mood, hours_since_last)
            full_system_prompt = f"{SYSTEM_PROMPT}\n\n🎭 CURRENT MOOD: {mood_context}"
            
            # Prepare messages with system prompt
            full_messages = [
                {"role": "system", "content": full_system_prompt}
            ] + messages
            
            # Get response from Ollama
            response = self.client.chat(
    model=self.model,
    messages=full_messages,
    stream=False,
    options={
        "temperature": 0.6,
        "num_predict": 150
    }
)

            
            return response['message']['content'].strip()
            
        except Exception as e:
            print(f"❌ Error communicating with AI: {e}")
            return "Sorry... I'm having trouble thinking right now. Can you try again?"
    
    def test_connection(self) -> bool:
        """Test if Ollama is running and model is available"""
        try:
            self.client.list()
            return True
        except Exception as e:
            print(f"❌ Cannot connect to Ollama: {e}")
            print("💡 Make sure Ollama is running: ollama serve")
            return False