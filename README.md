# Chandan Chatbot (Gemini-2.5-flash)

A simple desktop chatbot application built with Python, Tkinter, and Google Gemini (via the `google-generativeai` library). This chatbot provides a conversational interface using Google's Gemini LLM API.

## Features
- Modern Tkinter GUI with chat history and input box
- Asynchronous bot responses (no freezing UI)
- Uses Gemini-2.5-flash model for fast, high-quality answers
- Easily customizable for other Gemini models

## Requirements
- Python 3.8+
- Packages: `google-generativeai`, `tkinter`

## Installation
1. **Clone this repository or copy the files to your machine.**
2. **Set up a Python virtual environment (recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install google-generativeai tkinter
   ```
4. **Get a Google Gemini API key:**
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey) and create an API key.
   - Replace the `API_KEY` value in `main.py` with your key.

## Usage
Run the chatbot with:
```bash
python main.py
```
- Type your message in the input box and press Enter or click Send.
- The bot will reply using the Gemini model.
- To exit, simply close the window.

## How it Works
- The app uses Tkinter for the GUI.
- When you send a message, it calls the Gemini API using the `google-generativeai` library.
- Responses are shown in the chat window.
- All network calls are run in a background thread to keep the UI responsive.

## Customization
- Change the model by editing the `MODEL` variable in `main.py` (e.g., try `gemini-pro` or other available models).
- You can further style the GUI or add features as needed.

## Troubleshooting
- **No response or errors?**
  - Check your API key and internet connection.
  - Make sure you have the correct packages installed.
- **Tkinter not found?**
  - On some systems, you may need to install it separately (e.g., `sudo apt-get install python3-tk` on Ubuntu).

## License
This project is for educational/demo purposes. Please use your own API key and respect the terms of service for Google Gemini.
