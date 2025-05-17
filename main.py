import json
import os
import sys
from flask import Flask, request, jsonify, render_template
from dotenv import dotenv_values
from groq import Groq
import subprocess

from Backend.imagegeneration import GenerateSingleImage

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Backend'))

from Backend.texttospeech import TextToSpeech
from Backend.chatbot import Chatbot

app = Flask(__name__, template_folder='frontend/www', static_folder='frontend/static')

template_dir = os.path.join(os.getcwd(), 'frontend', 'www')
print(f"Looking for templates in: {template_dir}")
if not os.path.exists(template_dir):
    print(f"Template directory does not exist: {template_dir}")
else:
    print(f"Template directory found: {template_dir}")
    print(f"Files in template directory: {os.listdir(template_dir)}")

env_vars = dotenv_values(".env")
Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
AssistantVoice = env_vars.get("AssistantVoice")
GroqAPIKey = env_vars.get("GroqAPIKey")

if not GroqAPIKey:
    raise ValueError("GroqAPIKey is missing in the .env file.")

client = Groq(api_key=GroqAPIKey)

System = f"""Hello, I am {Username}, You are a very accurate and advanced excuse generator personal assistant named {Assistantname}.
*** Provide Answers In a professional way, make sure to add full stops, commas, question marks, and use proper grammar.***
*** Just answer the question from the provided data in a professional way. ***"""

def ensure_data_directory():
    os.makedirs("Data", exist_ok=True)
    data_file_path = os.path.join("Data", "ImageGeneration.data")
    if not os.path.exists(data_file_path):
        with open(data_file_path, "w") as f:
            f.write(",False")

ensure_data_directory()

def load_chat_history():
    try:
        os.makedirs('Data', exist_ok=True)
        with open(os.path.join('Data', 'Chatlog.json'), 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_chat_history(messages):
    os.makedirs('Data', exist_ok=True)
    with open(os.path.join('Data', 'Chatlog.json'), 'w', encoding='utf-8') as f:
        json.dump(messages, f, indent=4)


def handle_image_generation(query):
    try:
        data_file_path = os.path.join("Data", "ImageGeneration.data")
        with open(data_file_path, "w") as file:
            file.write(f"{query},True")

        from Backend.imagegeneration import process_image_generation
        process_image_generation()

        return f"Image generation request processed for query: {query}"

    except Exception as e:
        return f"Error generating image: {e}"

excuse_templates = {
    'legit': { ... },
    'mild': { ... },
    'chaos': { ... }
}

def generate_excuse(situation, tone):
    try:
        situation_map = {
            "Late to class": "class",
            "Missed assignment": "homework",
            "Missed exam": "presentation",
            "Skipped meeting": "group",
            "Forgot to reply": "group"
        }
        situation_key = situation_map.get(situation, "class")
        tone_key = tone.lower()

        excuses = excuse_templates.get(tone_key, {}).get(situation_key, [])
        if not excuses:
            return "Sorry, I couldn't find an excuse for this situation and tone."

        from random import choice
        return choice(excuses)

    except Exception as e:
        return f"Error generating excuse: {e}"

def chatbot(query):
    if query.lower().startswith("generate excuse"):
        try:
            parts = query.split(":", 1)
            if len(parts) < 2:
                return "Please specify the situation and tone in the format: 'generate excuse: situation, tone'."

            params = parts[1].strip().split(",")
            if len(params) < 2:
                return "Please specify both the situation and tone."

            situation = params[0].strip()
            tone = params[1].strip()

            return generate_excuse(situation, tone)

        except Exception as e:
            return f"Error processing excuse request: {e}"

    if query.lower().startswith("generate image"):
        image_prompt = query.replace("generate image", "").strip()
        return handle_image_generation(image_prompt)

    messages = load_chat_history()
    messages.append({"role": "user", "content": query})

    try:
        completion = client.chat.completions.create(
            model='llama3-70b-8192',
            messages=[{"role": "system", "content": System}] + messages,
            max_tokens=1024,
            temperature=0.7,
            top_p=1,
            stream=True,
            stop=None
        )

        answer = ""
        for chunk in completion:
            if chunk.choices[0].delta.content:
                answer += chunk.choices[0].delta.content

        answer = answer.replace("</s>", "").strip()
        messages.append({"role": "assistant", "content": answer})
        save_chat_history(messages)

        return answer

    except Exception as e:
        error_message = f"Error: {e}"
        print(error_message)
        return "I encountered an error. Please try again."

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Error rendering template: {str(e)}", 500


@app.route('/chats')
def chats():
    try:
        return render_template('chats.html')
    except Exception as e:
        return f"Error rendering template: {str(e)}", 500

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '')
    if not user_input:
        return jsonify({'error': 'No message provided'}), 400

    try:
        answer = chatbot(user_input)

        try:
            TextToSpeech(answer)
        except Exception as e:
            print(f"Warning: Text-to-speech failed: {e}")

        chat_history = load_chat_history()
        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": answer})
        save_chat_history(chat_history)

        return jsonify({'answer': answer})

    except Exception as e:
        print(f"Error processing chat: {e}")
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

@app.route('/chat-history', methods=['GET'])
def get_chat_history():
    chat_history = load_chat_history()
    return jsonify(chat_history)

if __name__ == "__main__":
    print(f"Holla Amigo! I am {Assistantname}. Access the app at http://localhost:5000")
    app.run(debug=True, host='localhost', port=5000)