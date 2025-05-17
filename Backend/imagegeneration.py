import asyncio
from random import randint
from PIL import Image
import requests
from dotenv import dotenv_values
import os
from time import sleep

def open_images(prompt):
    folder_path = r"Data"
    prompt = prompt.replace(" ", "_")

    Files = [f"{prompt}{i}.jpg" for i in range(1, 5)]

    for jpg_file in Files:
        image_path = os.path.join(folder_path, jpg_file)

        try:
            img = Image.open(image_path)
            print(f"Opening image: {image_path}")
            img.show()
            sleep(1)

        except IOError:
            print(f"Unable to open {image_path}")

env_vars = dotenv_values(".env")
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {env_vars['HuggingFaceAPIKey']}"}

async def query(payload):
    response = await asyncio.to_thread(requests.post, API_URL, headers=headers, json=payload)
    return response.content

async def generate_single_image(prompt: str):
    payload = {
        "inputs": f"{prompt}, quality=4k, sharpness=maximum, Ultra High Details, High Resolution, seed = {randint(0, 1000000)}",
    }
    image_bytes = await query(payload)
    image_path = os.path.join("Data", f"{prompt.replace(' ', '_')}.jpg")
    with open(image_path, "wb") as f:
        f.write(image_bytes)
    return image_path

def GenerateSingleImage(prompt: str):
    image_path = asyncio.run(generate_single_image(prompt))
    return image_path

# Remove the infinite loop
def process_image_generation():
    try:
        # Update the file path to the correct directory
        data_file_path = os.path.join("Data", "ImageGeneration.data")
        if not os.path.exists(data_file_path):
            with open(data_file_path, "w") as f:
                f.write(",False")

        with open(data_file_path, "r") as f:
            Data: str = f.read()

        Prompt, Status = Data.split(",")
        if Status.strip() == "True":
            print("Generating Images...")
            image_path = GenerateSingleImage(prompt=Prompt.strip())

            with open(data_file_path, "w") as f:
                f.write("False,False")

            print(f"Image generated successfully: {image_path}")
        else:
            print("No image generation request found.")

    except Exception as e:
        print(f"Error: {e}")