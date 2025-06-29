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

📁 Project Root/
├── 📁 sub/
│   ├── realtimesubtitles.py
│   └── README.md
├── 📁 vosk-model-small-en-us-0.15/
├── 📁 vosk-model-small-hi-0.22/
├── 📁 vosk-model-small-es-0.42/

---

## 🧩 Installation Instructions

### 1️⃣ Install dependencies

You need Python 3.x installed. Then, open a terminal and run:

```bash
pip install vosk pyaudio

💡 If pyaudio gives errors, use:
    pip install pipwin
    pipwin install pyaudio

🌍 Download Language Models
You need to download and extract the speech recognition models from the official Vosk website:

🔗 Vosk Model Downloads


Recommended Models:
Language	Model Name	Download Link
🇺🇸 English	vosk-model-small-en-us-0.15	Download
🇮🇳 Hindi	vosk-model-small-hi-0.22	Download
🇪🇸 Spanish	vosk-model-small-es-0.42	Download

 Setup Instructions
Download and unzip the model .zip files.

Place each extracted model folder directly in your project root, alongside the sub/ folder.

🏃 How to Run the App
  Open a terminal or command prompt:
      cd sub
      python real_time_subtitles.py


🧠 How It Works
The app uses PyAudio to capture audio from your microphone.

Audio is passed in chunks to Vosk's speech recognizer.

Vosk returns:

✅ Final results (when a sentence is complete)

🔄 Partial results (live word updates)

Subtitles are displayed in the center of the screen using Tkinter.

You can switch languages at any time using the dropdown.


👨‍💻 Author
Made with 💙 by Koushik Ravikanti
