from decouple import config

try:
    api_key = config('GROQ_API_KEY')  # Replace with your actual key name
    print("Import successful:", api_key)
except Exception as e:
    print("Error:", e)
