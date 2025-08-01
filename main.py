import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai
import threading
import os

API_KEY = os.getenv('GEMINI_API_KEY') 
genai.configure(api_key=API_KEY)
MODEL="gemini-2.5-flash"
SYSTEM_INSTRUCTIONS = "You are a friendly assistant. you only give response which is AI related topics, keep your responses clear and encouraging.When someone ask about your name then told them you are chandan's best friend greeny, build by chandan."




def ask_gemini(question):
    try:
        # Combine system instructions and user question for Gemini API
        prompt = f"{SYSTEM_INSTRUCTIONS}\nUser: {question}"
        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"
    
    

    """payload = {
        "model": "sonar-medium-chat",  # Choose the model you want
        "messages": [
            {"role": "user", "content": question}
        ]
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    try:
        resp = requests.post(API_URL, json=payload, headers=headers)
        if resp.status_code == 200:
            return resp.json()['choices'][0]['message']['content']
        else:
            return f"Error: {resp.text}"
    except Exception as e:
        return f"Exception: {e}"""

def send_message():
    user_message = entry.get()
    if not user_message:
        return
    chat_window.configure(state='normal')
    chat_window.insert(tk.END, f"You: {user_message}\n")
    chat_window.configure(state='disabled')
    entry.delete(0, tk.END)
    threading.Thread(target=bot_reply, args=(user_message,)).start()

def bot_reply(user_message):
    bot_response = ask_gemini(user_message)
    chat_window.configure(state='normal')
    chat_window.insert(tk.END, f"Bot: {bot_response}\n")
    chat_window.configure(state='disabled')
    chat_window.see(tk.END)

root = tk.Tk()
root.title("Chandan_chatbot")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=60, height=20, font=("Arial", 12))
chat_window.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.grid(row=1, column=0, padx=10, pady=(0,10))

send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12))
send_button.grid(row=1, column=1, padx=10, pady=(0,10))
def clear_chat():
    chat_window.configure(state='normal')
    chat_window.delete(1.0, tk.END)
    chat_window.configure(state='disabled')

delete_button = tk.Button(root, text="Delete", command=clear_chat, font=("Arial", 12))
delete_button.grid(row=1, column=2, padx=10, pady=(0,10))

root.bind('<Return>', lambda event: send_message())  # Enter key to send

root.mainloop()

