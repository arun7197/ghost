import subprocess as sp
from groq_speech_to_text import groq_recognize_speech  # Import the GROQ-based speech recognition
from voice_assistant.text_to_speech import speak
import time

query = groq_recognize_speech().lower()

if "open notepad" in query:
    speak("Opening notepad, sir")
    print("DEBUG: Attempting to open Notepad with subprocess...")
    time.sleep(1)  # Small delay before opening
    try:
        sp.Popen(["notepad.exe"])
        print("DEBUG: Notepad opened successfully with subprocess.")
    except Exception as e:
        speak(f"Sorry, I couldn't open Notepad due to: {e}")
        print(f"DEBUG: Error opening Notepad: {e}")
    time.sleep(2)  # Add extra delay after opening
