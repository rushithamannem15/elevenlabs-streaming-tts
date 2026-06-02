ElevenLabs Streaming Text-to-Speech

This project demonstrates real-time speech generation using the ElevenLabs Text-to-Speech Streaming API with Python.

Features:
Real-time audio streaming
Chunk-based playback
ElevenLabs REST API integration
PyAudio speaker playback
Environment variable support

Tech Stack:
Python
Requests
PyAudio
ElevenLabs API

SETUP:

Install dependencies:
pip install -r requirements.txt

Create .env file:
ELEVENLABS_API_KEY=your_api_key

Run:
python main.py

How It Works:
Sends text to ElevenLabs streaming endpoint
Receives PCM audio chunks
Plays chunks immediately using PyAudio
Continues until stream ends