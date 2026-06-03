import os
import requests
from dotenv import load_dotenv


def chunk_text(text, max_chars=3000):
    """
    Split large text into sentence-aware chunks.
    """

    sentences = text.split(". ")

    chunks = []
    current_chunk = ""

    for sentence in sentences:

        sentence = sentence.strip()

        # Add period back if missing
        if not sentence.endswith("."):
            sentence += "."

        sentence += " "

        # Check chunk size
        if len(current_chunk) + len(sentence) <= max_chars:
            current_chunk += sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence

    # Add remaining chunk
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.getenv("ELEVENLABS_API_KEY")

if not API_KEY:
    print("ERROR: ELEVENLABS_API_KEY not found in .env file")
    exit()

# Voice ID
VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"

# Output directory
OUTPUT_DIR = "audio_chunks"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Input text
TEXT = """
Hello, my name is Rushitha Mannem.

This project demonstrates scalable text-to-speech generation
using the ElevenLabs API and Python.

The application supports long-form text generation by splitting
large text into sentence-aware chunks, generating audio for each
chunk independently, and merging all generated audio into a
single final output file.

This architecture helps avoid provider character limit failures
while preserving natural speech flow and sentence boundaries.

The final merged audio is then played using FFmpeg and ffplay.
"""

# API endpoint
url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

# Request headers
headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

# Split text into chunks
text_chunks = chunk_text(TEXT)

print(f"Total chunks created: {len(text_chunks)}")

# Store generated audio file paths
audio_files = []

# Process each chunk
for index, chunk in enumerate(text_chunks):

    # Skip empty chunks
    if not chunk.strip():
        continue

    print(f"\nProcessing chunk {index + 1}...")

    payload = {
        "text": chunk,
        "model_id": "eleven_flash_v2_5"
    }

    try:

        # Streaming request
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            stream=True,
            timeout=60
        )

        # Error handling
        if response.status_code != 200:
            print(f"ERROR for chunk {index + 1}:")
            print(response.text)
            continue

        # Output file for chunk
        chunk_file = f"{OUTPUT_DIR}/chunk_{index + 1}.mp3"

        audio_files.append(chunk_file)

        print("Receiving audio chunks...")

        # Save streamed audio
        with open(chunk_file, "wb") as audio_file:

            for data in response.iter_content(chunk_size=4096):

                if data:
                    audio_file.write(data)

        print(f"Saved: {chunk_file}")

    except requests.exceptions.RequestException as e:
        print(f"Network error for chunk {index + 1}: {e}")

# Check if audio files exist
if not audio_files:
    print("No audio files generated.")
    exit()

print("\nMerging audio files...")

# Create FFmpeg concat list
with open("files.txt", "w") as file_list:

    for audio_file in audio_files:
        file_list.write(f"file '{audio_file}'\n")

# Merge all MP3 files
merge_command = (
    "ffmpeg -f concat -safe 0 "
    "-i files.txt -c copy final_output.mp3 -y"
)

merge_status = os.system(merge_command)

if merge_status != 0:
    print("ERROR: Failed to merge audio files.")
    exit()

print("Merged audio saved as final_output.mp3")

print("\nPlaying final audio...")

# Play final audio
play_command = "ffplay -nodisp -autoexit final_output.mp3"

os.system(play_command)

print("\nPlayback completed.")