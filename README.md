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

## ElevenLabs Streaming Text-to-Speech

This project demonstrates scalable real-time text-to-speech generation using the ElevenLabs API and Python.

The application supports long-form text generation by intelligently splitting large text into sentence-aware chunks, generating audio for each chunk independently, merging all generated audio files into a single final output, and playing the final audio using FFmpeg.

## Features
Real-time streaming request handling
Sentence-aware text chunking
Long-text scalability support
Multiple audio chunk generation
Automatic MP3 merging using FFmpeg
Final audio playback using ffplay
Environment variable support using .env
Error handling for failed requests
Clean and scalable project structure

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