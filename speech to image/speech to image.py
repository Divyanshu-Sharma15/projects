import openai
import requests
import json
import speech_recognition as sr
from pydub import AudioSegment
from PIL import Image

# Manually enter your API keys here
OPENAI_API_KEY = "your_openai_api_key"  # Replace with your actual OpenAI API key
MONSTERAPI_KEY = "your_monsterapi_key"  # Replace with your actual MonsterAPI key
MONSTERAPI_URL = "https://api.monsterapi.ai/v1/image/generate"

# Initialize OpenAI client
openai.api_key = OPENAI_API_KEY

# Function to convert speech to text using OpenAI Whisper
def speech_to_text(audio_path=None):
    recognizer = sr.Recognizer()

    if audio_path:  # Process pre-recorded file
        with open(audio_path, "rb") as audio_file:
            response = openai.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        return response.text  # Corrected response format

    else:  # Capture real-time microphone input
        with sr.Microphone() as source:
            print("Listening for speech...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            print("Processing...")

        try:
            with open("temp_audio.wav", "wb") as f:
                f.write(audio.get_wav_data())

            with open("temp_audio.wav", "rb") as audio_file:
                response = openai.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )
            return response.text
        except Exception as e:
            print(f"Error in speech recognition: {e}")
            return None

# Function to generate an image using MonsterAPI
def generate_image_from_text(prompt):
    headers = {
        "Authorization": f"Bearer {MONSTERAPI_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "negprompt": "deformed, bad anatomy, disfigured, poorly drawn face",
        "samples": 1,
        "steps": 50,
        "aspect_ratio": "square",
        "guidance_scale": 7.5,
        "seed": 2414,
    }
    
    response = requests.post(MONSTERAPI_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        image_url = response.json().get("image_url")
        print(f"Generated Image URL: {image_url}")
        
        # Download and show the image
        response = requests.get(image_url)
        if response.status_code == 200:
            file_name = "generated_image.png"
            with open(file_name, 'wb') as file:
                file.write(response.content)
            img = Image.open(file_name)
            img.show()
            print("Image downloaded and displayed successfully.")
        else:
            print("Failed to download the image.")
    else:
        print("Error generating image:", response.text)

# Main function to process speech and generate an image
def speech_to_image(audio_path=None):
    text_description = speech_to_text(audio_path)
    if text_description:
        print(f"Transcribed Text: {text_description}")
        generate_image_from_text(text_description)
    else:
        print("No valid text was extracted.")

# Run script
if __name__ == "__main__":
    user_choice = input("Enter 'file' to use an audio file or 'mic' to use the microphone: ").strip().lower()
    if user_choice == "file":
        audio_file_path = input("Enter the path to the audio file: ").strip()
        speech_to_image(audio_file_path)
    elif user_choice == "mic":
        speech_to_image()
    else:
        print("Invalid choice. Please enter 'file' or 'mic'.")