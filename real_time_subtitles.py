import tkinter as tk
from tkinter import ttk
from vosk import Model, KaldiRecognizer
import pyaudio
import json
import os

LANG_MODELS = {
    "🇺🇸 English": "../vosk-model-small-en-us-0.15",
    "🇮🇳 Hindi": "../vosk-model-small-hi-0.22",
    "IN Telugu": "../vosk-model-small-te-0.42",
}

current_model = None
recognizer = None

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,
                input=True, frames_per_buffer=8000)
stream.start_stream()

# ------------------- GUI Setup --------------------
root = tk.Tk()
root.title("🎤 SubLive - Real-Time Subtitles")
root.geometry("1000x550")
root.configure(bg="#2c3e50")  # Slate gray background


sidebar = tk.Frame(root, width=260, bg="#34495e")  # Blue-gray sidebar
sidebar.pack(side="left", fill="y")

# Logo/Title
tk.Label(sidebar, text="🎛️ SubLive Control Panel", font=("Segoe UI", 16, "bold"),
         fg="#ecf0f1", bg="#34495e", pady=20).pack()

# Language Dropdown
tk.Label(sidebar, text="🌐 Language", font=("Segoe UI", 12),
         fg="#ecf0f1", bg="#34495e").pack(pady=(10, 0))

lang_var = tk.StringVar()
lang_menu = ttk.Combobox(sidebar, textvariable=lang_var, font=("Segoe UI", 11),
                         values=list(LANG_MODELS.keys()), state="readonly", width=22)
lang_menu.set("🇺🇸 English")
lang_menu.pack(pady=10)

# Status Label
status_label = tk.Label(sidebar, text="🎧 Listening", font=("Segoe UI", 11, "bold"),
                        fg="#2ecc71", bg="#34495e")  # Green for listening
status_label.pack(pady=20)

# Info Footer
tk.Label(sidebar, text="\nMade with 💙 by Koushik", font=("Segoe UI", 9),
         fg="#bdc3c7", bg="#34495e").pack(side="bottom", pady=10)

# ------------------- Right Content Panel --------------------
content = tk.Frame(root, bg="#2c3e50")
content.pack(expand=True, fill="both")


subtitle_label = tk.Label(content, text="🎤 Say something...",
                          font=("Segoe UI", 24, "bold"), fg="#00bcd4",  # Sky blue
                          bg="#2c3e50", wraplength=680, justify="center")
subtitle_label.place(relx=0.5, rely=0.5, anchor="center")


def load_model(language_label):
    global current_model, recognizer
    model_path = LANG_MODELS[language_label]
    if not os.path.exists(model_path):
        subtitle_label.config(text=f" Model not found!\n{model_path}", fg="#ff6b6b")  # Coral red
        return
    current_model = Model(model_path)
    recognizer = KaldiRecognizer(current_model, 16000)
    subtitle_label.config(text=f" Loaded {language_label}\n🎤 Start Speaking!", fg="#00bcd4")

def on_language_change(event):
    load_model(lang_var.get())

lang_menu.bind("<<ComboboxSelected>>", on_language_change)

# ------------------- Subtitle Updater --------------------
def update_subtitles():
    if recognizer:
        data = stream.read(4000, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            subtitle_label.config(text=result.get("text", ""))
        else:
            partial = json.loads(recognizer.PartialResult())
            subtitle_label.config(text=partial.get("partial", ""))
    root.after(100, update_subtitles)

# ------------------- Start App --------------------
load_model(lang_var.get())  
root.after(100, update_subtitles)
root.mainloop()

