# ui/chat_cli.py
# import speech_recognition as sr
# import pyttsx3
from brain.responder import Responder
from config.settings import AI_NAME, VOICE_ENABLED, TTS_RATE, TTS_VOLUME
import sys
import speech_recognition as sr
import pyttsx3

class VoiceChat:
    """Voice-to-Voice chat interface"""
    
    def __init__(self):
        self.responder = Responder()
        self.recognizer = sr.Recognizer()
        self.tts_engine = None
        self.is_first_message = True
        
        if VOICE_ENABLED:
            self._init_tts()
    
    def _init_tts(self):
        """Initialize text-to-speech engine"""
        try:
            self.tts_engine = pyttsx3.init()
            self.tts_engine.setProperty('rate', TTS_RATE)
            self.tts_engine.setProperty('volume', TTS_VOLUME)
            
            # Try to set a female voice
            voices = self.tts_engine.getProperty('voices')
            for voice in voices:
                if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
                    self.tts_engine.setProperty('voice', voice.id)
                    break
            
            print("🔊 Voice enabled")
        except Exception as e:
            print(f"⚠️ Could not initialize voice: {e}")
            self.tts_engine = None
    
    def speak(self, text: str):
        """Speak the text using TTS"""
        if self.tts_engine and VOICE_ENABLED:
            try:
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()
            except Exception as e:
                print(f"⚠️ TTS Error: {e}")
    
    def listen(self) -> str:
        """Listen to user's voice and convert to text"""
        try:
            with sr.Microphone() as source:
                print("🎤 Listening... (speak now)")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                
            print("🔄 Processing...")
            text = self.recognizer.recognize_google(audio)
            return text
            
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            print("❓ Sorry, I couldn't understand that")
            return None
        except sr.RequestError as e:
            print(f"❌ Speech recognition error: {e}")
            return None
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
    
    def run_voice_mode(self):
        """Run continuous voice conversation"""
        mood_emoji = self.responder.get_current_mood_emoji()
        print(f"\n{'='*60}")
        print(f"💖 {AI_NAME} is ready to talk! {mood_emoji}")
        print(f"{'='*60}")
        print("\n📌 Commands:")
        print("   - Say 'goodbye' or 'bye' to exit")
        print("   - Say 'text mode' to switch to typing")
        print("   - Press Ctrl+C to force quit\n")
        
        # Initial greeting
        greeting = self.responder.respond("Hello!", is_greeting=True)
        print(f"\n{AI_NAME} {mood_emoji}: {greeting}\n")
        self.speak(greeting)
        
        self.is_first_message = False
        
        while True:
            try:
                # Listen to user
                user_input = self.listen()
                
                if user_input is None:
                    continue
                
                print(f"You: {user_input}")
                
                # Check for exit commands
                if user_input.lower() in ['goodbye', 'bye', 'exit', 'quit']:
                    farewell = self.responder.respond(user_input)
                    print(f"\n{AI_NAME} {mood_emoji}: {farewell}\n")
                    self.speak(farewell)
                    break
                
                # Check for mode switch
                if 'text mode' in user_input.lower():
                    print("\n📝 Switching to text mode...")
                    return 'text'
                
                # Get AI response
                response = self.responder.respond(user_input)
                mood_emoji = self.responder.get_current_mood_emoji()
                
                print(f"\n{AI_NAME} {mood_emoji}: {response}\n")
                self.speak(response)
                
            except KeyboardInterrupt:
                print("\n\n👋 Interrupted by user. Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                continue
    
    def run_text_mode(self):
        """Run text-based conversation"""
        mood_emoji = self.responder.get_current_mood_emoji()
        print(f"\n{'='*60}")
        print(f"💖 {AI_NAME} is ready to chat! {mood_emoji}")
        print(f"{'='*60}")
        print("\n📌 Commands:")
        print("   - Type 'voice mode' to switch to voice")
        print("   - Type 'bye' or 'exit' to quit")
        print("   - Press Ctrl+C to force quit\n")
        
        # Initial greeting
        greeting = self.responder.respond("Hi there!", is_greeting=True)
        print(f"\n{AI_NAME} {mood_emoji}: {greeting}\n")
        
        self.is_first_message = False
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                # Check for exit commands
                if user_input.lower() in ['bye', 'exit', 'quit', 'goodbye']:
                    farewell = self.responder.respond(user_input)
                    print(f"\n{AI_NAME} {mood_emoji}: {farewell}\n")
                    break
                
                # Check for mode switch
                if user_input.lower() == 'voice mode':
                    print("\n🎤 Switching to voice mode...")
                    return 'voice'
                
                # Get AI response
                response = self.responder.respond(user_input)
                mood_emoji = self.responder.get_current_mood_emoji()
                
                print(f"\n{AI_NAME} {mood_emoji}: {response}\n")
                
            except KeyboardInterrupt:
                print("\n\n👋 Interrupted by user. Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                continue