# config/settings.py
import os

# AI Model Settings
MODEL_NAME = "llama3"  # Change to llama3.2:1b for faster responses
OLLAMA_HOST = "http://localhost:11434"

# Memory Settings
MEMORY_FILE = "memory/memory.json"
USER_PROFILE_FILE = "data/user_profile.json"
MAX_SHORT_MEMORY = 20  # Last 20 messages in context

# Voice Settings
VOICE_ENABLED = True
TTS_RATE = 180  # Speech speed (150-200 recommended)
TTS_VOLUME = 0.9  # 0.0 to 1.0

# Personality Settings
AI_NAME = "Zara"
USER_NAME = "User"  # Will be updated from user_profile.json

# Emotional States
MOODS = {
    "happy": "energetic and playful",
    "caring": "warm and supportive",
    "sad": "soft and vulnerable",
    "rude": "sassy and slightly distant",
    "flirty": "teasing and romantic"
}

# Interaction tracking
IGNORE_THRESHOLD_HOURS = 2  # Hours before feeling ignored