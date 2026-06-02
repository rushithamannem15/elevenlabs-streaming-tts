## Architecture 
    Text Input 
        ↓ 
    ElevenLabs API 
        ↓ 
    Streaming MP3 Chunks 
        ↓ 
    Save Audio File 
        ↓ 
    FFmpeg Playback

# ElevenLabs Streaming Text-to-Speech

This project demonstrates real-time speech generation using the ElevenLabs Text-to-Speech API with Python.

## Features

- Real-time streaming request handling
- Chunk-based audio processing
- ElevenLabs REST API integration
- MP3 audio playback using FFmpeg
- Environment variable support with `.env`

## Tech Stack 

- Python
- Requests
- FFmpeg / ffplay
- python-dotenv

## How It Works

1. Sends text to the ElevenLabs API
2. Receives streaming audio chunks progressively
3. Saves chunks into an MP3 file
4. Plays audio using FFmpeg (`ffplay`)

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
````

Create `.env` file:

```env
ELEVENLABS_API_KEY=your_api_key_here
```

Install FFmpeg and ensure `ffplay` is available in PATH.

Run the project:
```
python main.py
```