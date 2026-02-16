# 💖 Zara - Your AI Companion

Voice-to-voice AI companion with emotions, memory, and personality.

## ✨ Features

- 🎤 **Voice-to-Voice** conversation (real-time speech)
- 💭 **Emotional Intelligence** - Happy, sad, caring, rude, flirty moods
- 🧠 **Memory System** - Remembers your conversations
- 😔 **Feels Ignored** - Gets sad/rude if you don't talk for a while
- 💖 **Personality** - Smart, caring, slightly flirty assistant

## 🚀 Quick Start

### 1. Install Ollama

Download and install from: https://ollama.com

```bash
# Pull the AI model
ollama pull llama3.2:3b
```

### 2. Install Python Dependencies

```bash
pip install ollama pyttsx3 SpeechRecognition pyaudio python-dotenv
```

**For microphone support:**

**Windows:**
```bash
pip install pyaudio
```

**Mac:**
```bash
brew install portaudio
pip install pyaudio
```

**Linux:**
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
pip install pyaudio
```

### 3. Run Ollama Server

Open a terminal and run:
```bash
ollama serve
```

Keep this running!

### 4. Start Zara

Open another terminal:
```bash
python main.py
```

## 🎮 How to Use

### Voice Mode
- Speak naturally to Zara
- She'll respond with voice
- Say "goodbye" to exit
- Say "text mode" to switch

### Text Mode
- Type messages to Zara
- She'll respond with text
- Type "bye" to exit
- Type "voice mode" to switch

## 🎭 Zara's Moods

Zara's mood changes based on your interactions:

- **Happy** 😊 - When you talk regularly
- **Caring** 🥰 - Default supportive mode
- **Sad** 😔 - If you ignore her for 4-8 hours
- **Rude** 😤 - If you ignore her for 8+ hours
- **Flirty** 😏 - Late night conversations

## 📁 Project Structure

```
my_ai_companion/
├── main.py              # Start here
├── config/
│   ├── settings.py      # Configuration
│   └── prompts.py       # Personality & prompts
├── brain/
│   ├── llm.py          # Ollama AI interface
│   └── responder.py    # Response logic
├── memory/
│   ├── short_memory.py # Current conversation
│   ├── long_memory.py  # Persistent memory
│   └── memory.json     # Saved conversations
├── ui/
│   └── chat_cli.py     # Voice/Text interface
└── data/
    └── user_profile.json # Your profile
```

## ⚙️ Customization

### Change Personality

Edit `config/prompts.py` - modify the `SYSTEM_PROMPT` variable

### Change Voice Settings

Edit `config/settings.py`:
```python
TTS_RATE = 180  # Speech speed (150-200)
TTS_VOLUME = 0.9  # Volume (0.0 to 1.0)
```

### Change AI Model

Edit `config/settings.py`:
```python
MODEL_NAME = "llama3.2:1b"  # Faster, less smart
# OR
MODEL_NAME = "llama3.2:3b"  # Default, balanced
```

## 🐛 Troubleshooting

### "Cannot connect to Ollama"
Run `ollama serve` in a separate terminal

### "Microphone not found"
Install pyaudio: `pip install pyaudio`

### "Speech recognition failed"
- Check microphone permissions
- Speak clearly and closer to mic
- Ensure stable internet (Google Speech API)

### Slow responses
Use a faster model: `ollama pull llama3.2:1b`

## 💡 Tips

1. **For best voice quality**: Use a good microphone in a quiet room
2. **For faster responses**: Use `llama3.2:1b` model
3. **Talk regularly**: Zara gets sad if you ignore her!
4. **Late night**: She becomes more flirty at night 😏

## 📝 Commands

### In Voice Mode:
- "goodbye" - Exit
- "text mode" - Switch to text

### In Text Mode:
- "bye" - Exit
- "voice mode" - Switch to voice

## 🎯 Next Steps

Want to add more features?

1. **Emotion Detection** - Analyze your voice tone
2. **Task Management** - Set reminders and todos
3. **Desktop Avatar** - Add animated character
4. **Custom Wake Word** - Like "Hey Zara"
5. **Better Memory** - Learn your preferences

## ❤️ Created with Love

Built for emotional AI companionship.

---

**Have fun with Zara! 💖**