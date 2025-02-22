import speech_recognition as sr
import subprocess
import os
import time
from decouple import config  # To fetch the API key from the .env file
from groq import Groq  # Assuming the Groq API client is available
from voice_assistant.text_to_speech import speak  # Assuming text_to_speech is defined here

# Fetch the API key from the environment
api_key = config('GROQ_API_KEY')

# Function to generate a response using the GROQ model
def _generate_groq_response(chat_history):
    client = Groq(api_key=api_key)
    
    # Add a system message to enforce the assistant behavior
    system_message = {
        "role": "system",
        "content": "You are a helpful assistant. Always respond in short answers and address the user as 'boss'."
    }
    
    # Insert the system message at the beginning of the conversation history
    chat_history.insert(0, system_message)
    
    # Call the GROQ model to generate a response based on the conversation history
    response = client.chat.completions.create(
        model="llama3-8b-8192",  # Replace this with the actual model name you have access to
        messages=chat_history
    )
    
    return response.choices[0].message.content

# Function for handling speech recognition and returning the GROQ-generated response
def groq_recognize_speech():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        # Recognize the speech using Google Speech Recognition
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query
    
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand that."
    
    except sr.RequestError as e:
        return f"Could not request results; {e}"
    
    except Exception as e:
        return f"An error occurred: {e}"
