from elevenlabs import Voice, VoiceSettings, play
from elevenlabs import play
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
  api_key="sk_8c274c9a2b8d04c3370f5456a776d4309abf6e74af9646f0", # Defaults to ELEVEN_API_KEY
)

audio = client.generate(
    text= "Hi,I'm Tony Stark",
    voice=Voice(
        voice_id='EXAVITQu4vr4xnSDxMaL',
        settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
    )
)

play(audio)