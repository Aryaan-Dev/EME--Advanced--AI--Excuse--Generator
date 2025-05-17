# Advanced AI Excuse Generator ( EME ) 🤖✨

Welcome to the Advanced AI Excuse Generator (EME), a fun project that uses AI to create clever and believable excuses for any situation! Need a reason for being late or missing a deadline ? EME has you covered with a sleek web interface and animated excuses. This project is perfect for anyone who wants to explore AI and web development. 🚀

This README will walk you through setting up and running the project on your computer. Let’s get started !

---

## Prerequisites 🛠️

Before you start, make sure you have the following installed on your computer:

- **Python 3.8+** (Download from python.org if you don’t have it)
- A modern web browser (Chrome, Firefox, etc.)

---

## Screenshots 📸

![Alt text]()

---

## Folder Structure 📂

Make sure your project folder looks like this after cloning from GitHub:

```
eme_excuse_generator/
├── .venv/                       # Virtual environment folder (you’ll create this)
│
├── Backend/
│      ├── chatbot.py
│      ├── imagegeneration.py
│      ├── model.py
│      └── texttospeech.py
│
├── Data/
│      ├── Chatlog.json
│      ├── imagegeneration.data
│      ├── speech.mp3
│      └── Voice.html
│
├── frontend/
│        ├── static/
│        │        ├── main.js
│        │        ├── script.js
│        │        └── style.jss
│        │
│        └── www/
│              ├── assets/
│              │        ├── vondore/
│              │        │       └── textlate/
│              │        │                ├── img/
│              │        │                │     └── Eme.ico
│              │        │                ├── animate.css
│              │        │                ├── style.css
│              │        │                ├── jquery.fittext.js
│              │        │                └── jquery.lattering.js
│              │        └── jquery.min.js
│              │
│              ├── chats.html
│              ├── index.html
│              ├── Voice.html
│              ├── style.css
│              ├── main.js
│              └── script.js
│
├── .env                      # Make sure to add the API keys correctly
├── main.py
├── requirements.txt          # Required dependencies to run the program
└── README.md                 # This file
```

---

## Setup Instructions 🚀

Follow these steps to get the project running on your computer:

### 1. Clone the Repository 📥

Clone the `eme_excuse_generator` repository from GitHub to your computer:

```bash
git clone https://github.com/your-username/eme_excuse_generator.git
```

Navigate to the project folder:

```bash
cd eme_excuse_generator
```

### 2. Create a Virtual Environment 🌟

Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux) and create a virtual environment to manage the project’s dependencies:

```bash
python -m venv .venv
```

Activate the virtual environment:

- **Windows**:

  ```bash
  .venv\Scripts\activate
  ```

- **Mac/Linux**:

  ```bash
  source .venv/bin/activate
  ```

You’ll see `(.venv)` in your terminal, which means the virtual environment is active. 🎉

### 3. Install Python Dependencies 📦

Install the required Python packages (we’ll use Flask for the backend):

If `requirements.txt` exists, run:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, create it with this command:

```bash
echo "Flask==2.3.2" > requirements.txt
pip install -r requirements.txt
```

### 4. Run the Project 🌐

With the virtual environment activated, start the server:

```bash
python main.py
```

The server will run on `http://localhost:5000`. **Keep the terminal open.**

### 5. Open the Project 🎉

Open your web browser and go to `http://localhost:5000`. You’ll see the EME Excuse Generator in action ! 😄

---

## Troubleshooting 🛠️

If something goes wrong, try these fixes:

- **Error: "ModuleNotFoundError: No module named 'Flask'"**

  - Make sure the virtual environment is activated (`(.venv)` in terminal).
  - Reinstall dependencies: `pip install -r requirements.txt`.

- **Button doesn’t work when clicked**

  - Ensure `main.py` is running (`python main.py`).
  - Open your browser’s developer tools (F12) and check the console for errors.

- **Animations aren’t working**

  - Confirm that `animate.css` and `style.css` are linked in `index.html`.
  - Make sure jQuery, Lettering.js, and FitText.js load before `main.js`.

- **Port already in use**

  - If `http://localhost:5000` doesn’t work, another app might be using that port. Change the port in `main.py`:

    ```python
    app.run(debug=True, port=5001)
    ```

  - Then visit `http://localhost:5001` instead.

- **Can’t find the project files**

  - Double-check that you’ve cloned the entire `eme_excuse_generator` repository from GitHub.

- **Still stuck ?** 😕

  - Check the folder structure and file contents carefully.
  - Reach out to the project creator for help !

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Made By 👨‍💻

Created with ❤️ by  **B P ARYAAN \[ ARYAAN-DEV \]**. I hope you enjoy using the EME (AI Excuse Generator) as much as I enjoyed building it !

Have fun and may your excuses always save the day !
