# main.py
from ui.chat_cli import VoiceChat
from brain.responder import Responder
from config.settings import AI_NAME, VOICE_ENABLED
import sys

def print_banner():
    """Print startup banner"""
    print("\n" + "="*60)
    print(f"💖 Welcome to {AI_NAME} - Your AI Companion")
    print("="*60)

def check_dependencies():
    """Check if required services are running"""
    from brain.llm import AIBrain
    
    brain = AIBrain()
    if not brain.test_connection():
        print("\n❌ Cannot connect to Ollama!")
        print("Please start Ollama first:")
        print("   1. Open terminal")
        print("   2. Run: ollama serve")
        print("   3. Then run this program again\n")
        return False
    return True

def setup_user():
    """Initial user setup"""
    from memory.long_memory import LongMemory
    
    memory = LongMemory()
    user_name = memory.get_user_name()
    
    if user_name == "User":
        print(f"\n👋 Hi! I'm {AI_NAME}. What's your name?")
        name = input("Your name: ").strip()
        if name:
            memory.set_user_name(name)
            print(f"\n💖 Nice to meet you, {name}!\n")
        else:
            print(f"\n💖 Okay, I'll call you User for now!\n")

def choose_mode() -> str:
    """Let user choose chat mode"""
    if not VOICE_ENABLED:
        return 'text'
    
    print("\n🎯 Choose your mode:")
    print("   1. Voice Mode (Talk to Zara)")
    print("   2. Text Mode (Type to Zara)")
    
    while True:
        choice = input("\nEnter 1 or 2: ").strip()
        if choice == '1':
            return 'voice'
        elif choice == '2':
            return 'text'
        else:
            print("Please enter 1 or 2")

def main():
    """Main entry point"""
    print_banner()
    
    # Check if Ollama is running
    if not check_dependencies():
        sys.exit(1)
    
    # Setup user profile
    setup_user()
    
    # Choose initial mode
    current_mode = choose_mode()
    
    # Start chat
    chat = VoiceChat()
    
    while True:
        try:
            if current_mode == 'voice':
                result = chat.run_voice_mode()
                if result == 'text':
                    current_mode = 'text'
                    continue
                else:
                    break
            else:  # text mode
                result = chat.run_text_mode()
                if result == 'voice':
                    current_mode = 'voice'
                    continue
                else:
                    break
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
            break
    
    print(f"\n💖 Thanks for talking to me! Come back soon!\n")

if __name__ == "__main__":
    main()