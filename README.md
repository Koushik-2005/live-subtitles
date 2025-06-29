
# 🎤 Real-Time Subtitles Generator (SubLive)

SubLive is a Python-based real-time speech-to-text subtitle generator. It listens to your microphone and displays live transcriptions using the [Vosk](https://alphacephei.com/vosk/) offline speech recognition engine. It supports multiple languages with a simple and modern graphical user interface.

---

## 🚀 Features

- 🧠 Real-time transcription from your microphone  
- 🌐 Multi-language model switching  
- 🎛️ Beautiful, emoji-enhanced GUI with Tkinter  
- 📦 Fully offline (after downloading the models)  
- 💬 Live partial and final subtitle updates  

---

## 🛠️ Tech Stack

- Python 3.x  
- Tkinter (for GUI)  
- PyAudio (for microphone input)  
- Vosk (for speech recognition)  

---

## 📁 Project Structure

```
Project Root/
├── sub/
│   ├── realtimesubtitles.py
│   └── README.md
├── vosk-model-small-en-us-0.15/
├── vosk-model-small-hi-0.22/
├── vosk-model-small-te-0.42/
```

---

## 🧩 Installation Instructions

### 1️⃣ Install dependencies

Ensure Python 3.x is installed. Then run:

```bash
pip install vosk pyaudio
```

If `pyaudio` gives errors on Windows:

```bash
pip install pipwin
pipwin install pyaudio
```

---

### 🌍 Download Language Models

You need to download and extract the speech recognition models from the official Vosk website: [Vosk Models](https://alphacephei.com/vosk/models)

#### Recommended Models:

| Language | Model Name                  | Download Link |
|----------|-----------------------------|----------------|
| 🇺🇸 English | vosk-model-small-en-us-0.15 | [Download](https://alphacephei.com/vosk/models) |
| 🇮🇳 Hindi   | vosk-model-small-hi-0.22    | [Download](https://alphacephei.com/vosk/models) |
| 🇪🇸 Spanish | vosk-model-small-es-0.42   | [Download](https://alphacephei.com/vosk/models) |

Extract the downloaded zip files and place the folders directly inside your **Project Root**, alongside the `sub/` folder.

---

## 🏃 How to Run the App

```bash
cd sub
python realtimesubtitles.py
```

---

## 🧠 How It Works

- Captures audio using PyAudio  
- Sends chunks of audio to Vosk's recognizer  
- Displays live and final results using Tkinter  
- Supports language switching via dropdown  

---
🖼️ Screenshots
  ![Screenshot 2025-06-29 134708](https://github.com/user-attachments/assets/769c7405-cc85-43f0-9ad8-03d9d96d7b7f)

---


## 👨‍💻 Author

Made with 💙 by **Sri Koushik Ravikanti**
