🌸 Waifu AI – Anime Style Voice Assistant

Python 3.11+ | OpenRouter API | Edge-TTS | Tkinter GUI | Voice Assistant

🚀 Project Overview

Waifu AI is an anime-style virtual assistant that listens, talks, opens websites, searches, explains topics, sets timers, and interacts using cute anime voices like Nanami, Neerja, and Jenny.

This project started from an Instagram reel inspiration and evolved into a complete AI desktop assistant with voice + GUI.

<p align="center">
  <img src="https://raw.githubusercontent.com/HARINII2415/Waifu-AI-Anime-Chatbot/main/elf2.gif" width="350" alt="Waifu AI Banner">
</p>

🛠️ Features

🎤 Voice recognition (Press F2 to speak)

🎧 Anime-style TTS (Japanese / English / Indian voices)

🤖 AI chat using OpenRouter

🌐 Opens any website (YouTube, Google, Instagram…)

🔍 Searches on Google, YouTube, ChatGPT

📚 Wikipedia “Explain / Who is”

🎶 Spotify search

🔁 Repeat-after-me

⏰ Timers

💬 Small talk responses

🎨 Tkinter GUI with animated GIF

⚡ Both EXE + Python versions

📦 Requirements
Python 3.10+
edge-tts
playsound
SpeechRecognition
pygetwindow
pyautogui
wikipedia
Pillow
requests
tkinter


Install:

pip install -r requirements.txt

🧩 Code Structure
waifuaichatbot/
│
├── horiAI.py              # Online version (API)
├── waifuAI.py             # Offline EXE version
├── waifuAI.exe            # Ready-to-run executable
├── responses4u.py         # Custom small-talk replies
├── requirements.txt       # Dependencies
├── elf2.gif               # GUI background animation
├── voices.txt             # EdgeTTS voices
└── User Guide.txt         # Documentation

💡 How It Works (Short)

Press F2 → AI listens

Speech → text (SpeechRecognition)

AI generates reply (OpenRouter)

Text → anime voice (Edge-TTS)

GUI displays conversation

Assistant executes commands

▶️ Running
Online (Hori)
python horiAI.py

Offline (Wifu EXE)

Double-click:

waifuAI.exe

🔐 Add Your API Key

Inside horiAI.py:

OPENROUTER_API_KEY = "your_api_key_here"

🤝 Contributions

Feel free to fork, submit PRs, and improve the project!

📫 Contact

Created by Harini A
📧 harinii2415@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/harini-a-9a014925a/

Happy Coding & Creating! 🌸🚀💖
