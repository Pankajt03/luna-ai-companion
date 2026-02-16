# memory/long_memory.py
import json
from datetime import datetime
from pathlib import Path
from config.settings import MEMORY_FILE, USER_PROFILE_FILE, AI_NAME

class LongMemory:
    """Manages persistent memory across sessions"""
    
    def __init__(self):
        self.memory_path = Path(MEMORY_FILE)
        self.profile_path = Path(USER_PROFILE_FILE)
        self._ensure_files_exist()
        self.memory_data = self._load_memory()
        self.profile_data = self._load_profile()
    
    def _ensure_files_exist(self):
        """Create memory and profile files if they don't exist"""
        # Create memory.json
        if not self.memory_path.exists():
            self.memory_path.parent.mkdir(parents=True, exist_ok=True)
            default_memory = {
                "last_interaction": None,
                "conversation_history": [],
                "total_conversations": 0
            }
            with open(self.memory_path, 'w', encoding='utf-8') as f:
                json.dump(default_memory, f, indent=2, ensure_ascii=False)
        
        # Create user_profile.json
        if not self.profile_path.exists():
            self.profile_path.parent.mkdir(parents=True, exist_ok=True)
            default_profile = {
                "name": "User",
                "preferences": {},
                "created_at": datetime.now().isoformat()
            }
            with open(self.profile_path, 'w', encoding='utf-8') as f:
                json.dump(default_profile, f, indent=2, ensure_ascii=False)
    
    def _load_memory(self) -> dict:
        """Load memory from file"""
        try:
            with open(self.memory_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Error loading memory: {e}")
            return {
                "last_interaction": None,
                "conversation_history": [],
                "total_conversations": 0
            }
    
    def _load_profile(self) -> dict:
        """Load user profile from file"""
        try:
            with open(self.profile_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Error loading profile: {e}")
            return {"name": "User", "preferences": {}}
    
    def _save_memory(self):
        """Save memory to file"""
        try:
            with open(self.memory_path, 'w', encoding='utf-8') as f:
                json.dump(self.memory_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️ Error saving memory: {e}")
    
    def _save_profile(self):
        """Save profile to file"""
        try:
            with open(self.profile_path, 'w', encoding='utf-8') as f:
                json.dump(self.profile_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️ Error saving profile: {e}")
    
    def update_last_interaction(self):
        """Update last interaction timestamp"""
        self.memory_data["last_interaction"] = datetime.now().isoformat()
        self._save_memory()
    
    def get_last_interaction_time(self) -> datetime:
        """Get last interaction as datetime object"""
        last = self.memory_data.get("last_interaction")
        if last:
            return datetime.fromisoformat(last)
        return None
    
    def save_conversation(self, user_msg: str, ai_msg: str):
        """Save conversation exchange"""
        conversation = {
            "timestamp": datetime.now().isoformat(),
            "user": user_msg,
            "assistant": ai_msg
        }
        
        if "conversation_history" not in self.memory_data:
            self.memory_data["conversation_history"] = []
        
        self.memory_data["conversation_history"].append(conversation)
        self.memory_data["total_conversations"] = len(self.memory_data["conversation_history"])
        
        # Keep only last 100 conversations to prevent file bloat
        if len(self.memory_data["conversation_history"]) > 100:
            self.memory_data["conversation_history"] = self.memory_data["conversation_history"][-100:]
        
        self._save_memory()
    
    def get_user_name(self) -> str:
        """Get user's name"""
        return self.profile_data.get("name", "User")
    
    def set_user_name(self, name: str):
        """Set user's name"""
        self.profile_data["name"] = name
        self._save_profile()
    
    def get_conversation_count(self) -> int:
        """Get total conversation count"""
        return self.memory_data.get("total_conversations", 0)