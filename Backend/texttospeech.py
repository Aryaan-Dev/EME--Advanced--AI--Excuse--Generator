import pygame
import asyncio
import edge_tts
import os
import logging
from dotenv import dotenv_values

# Load environment variables
env_vars = dotenv_values(".env")
AssistantVoice = env_vars.get("AssistantVoice")

# Async function to generate TTS audio file
async def TTS(text, voice, file_path):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(file_path)

# Function to handle Text-to-Speech
def TextToSpeech(text):
    try:
        print(f"EME: {text}")
        voice = AssistantVoice or os.getenv('AssistantVoice')  # Fallback to environment variable
        file_path = os.path.join("Data", "speech.mp3")

        # Ensure the Data directory exists
        os.makedirs("Data", exist_ok=True)

        # Generate the audio file
        asyncio.run(TTS(text, voice, file_path))

        # Play the audio file
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Wait until the audio finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        logging.warning(f"Text-to-Speech failed: {e}")

    finally:
        # Clean up the pygame mixer
        try:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except Exception as e:
            logging.warning(f"Error during pygame cleanup: {e}")

# Test the TextToSpeech function
if __name__ == "__main__":
    while True:
        TextToSpeech(input("Enter the words: "))




