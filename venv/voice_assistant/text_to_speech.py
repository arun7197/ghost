from elevenlabs import Voice, VoiceSettings, play
from elevenlabs import play
from elevenlabs.client import ElevenLabs

def speak(text):
    client = ElevenLabs(
      api_key="sk_75b9a9d00ec58453d1f8150d3d34d93bc547191024109602", # Ensure this API key is valid
    )
    
    audio = client.generate(
        text=text,  # Use the passed text argument
        voice=Voice(
            voice_id='EXAVITQu4vr4xnSDxMaL',
            settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
        )
    )
    
    if audio:
        play(audio)
    else:
        print("No audio generated")