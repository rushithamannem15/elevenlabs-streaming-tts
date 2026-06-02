import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Voice ID
VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"

# Input text
TEXT = """
Hello, My name is Rushitha Mannem and this is my assignment to play the text to speech audio using ElevenLabs API and Python.
"""

# API endpoint
url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

# Request headers
headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

# Request payload
payload = {
    "text": TEXT,
    "model_id": "eleven_flash_v2_5"
}

print("Sending request to ElevenLabs...")

# Streaming request
response = requests.post(
    url,
    json=payload,
    headers=headers,
    stream=True
)

# Error handling
if response.status_code != 200:
    print("Error:", response.text)
    exit()

print("Receiving audio chunks...")

# Save streamed chunks into mp3 file
with open("output.mp3", "wb") as audio_file:

    for chunk in response.iter_content(chunk_size=4096):

        if chunk:
            audio_file.write(chunk)

print("Audio saved as output.mp3")

print("Playing audio...")

# Play audio using ffplay
os.system("ffplay -nodisp -autoexit output.mp3")

print("Playback completed.")