🌸 Waifu AI – Anime Voice Assistant
Your personal anime-style AI companion built with Python
<p align="center"> <img src="https://i.imgur.com/sS6wXbb.gif" width="400px" /> </p>
💠 Overview

Waifu AI is an anime-inspired voice assistant capable of talking, listening, understanding natural language, opening apps, searching, setting timers, and performing real-time tasks — all with a cute anime-style voice like Nanami, Neerja, or Jenny Neural.

This project was built after a random Instagram reel inspired me to explore voice AI — and it turned into one of my most fun and creative builds so far 💞.

🎀 Features
🗣️ Anime-style Voice Output

Natural Japanese voice (ja-JP-NanamiNeural)

Indian English voice (en-IN-NeerjaNeural)

American English voice (en-US-JennyNeural)

🔊 Real-time Speech Recognition

Trigger the mic using F2

Converts your voice into text instantly

🤖 Smart Conversations

Powered by OpenRouter AI API

Understands commands + engages in cute small talk

🌐 Web Automation

Say commands like:

“Open YouTube"

“Search anime fights on YouTube”

“Search AI tools on Google”

🎶 Spotify Integration

Searches for your song

Opens it on Spotify

(User presses play due to latest Spotify update)

📚 Wikipedia Integration

“Who is Elon Musk?”

“Explain quantum physics”

“Define blockchain”

⏰ Timers

“Set timer for 10 seconds”

“Set timer for 2 minutes”

🎥 Beautiful Animated GUI

Uses Tkinter + GIF animation

Custom-built UI with aesthetic colors

💾 Two Versions Available
Version	Description
Wifu (EXE)	Offline version, runs without Python
Hori (API)	Online version with natural speech + AI chat
🧠 Tech Stack

Python 3.11+

Microsoft Edge TTS

SpeechRecognition

Tkinter GUI

Wikipedia API

OpenRouter AI

PyInstaller (for EXE build)

📦 Installation (Hori – Online Version)
git clone https://github.com/HARINII2415/Waifu-AI-Anime-Chatbot/
cd waifuaichatbot

1️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Add Your API Key

Open horiAI.py and replace:

OPENROUTER_API_KEY = "your_api_key_here"

4️⃣ Run the Project
python horiAI.py

💻 Running the EXE (Offline Version)

Download the EXE from the repo or release page

Double-click waifuAI.exe

Enjoy your anime assistant 💕

🗂️ Project Structure
waifuaichatbot/
│
├── horiAI.py              # Online AI version
├── waifuAI.py             # Offline version
├── waifuAI.exe            # Compiled EXE
├── responses4u.py         # Custom response mappings
├── requirements.txt       # Dependencies
├── elf2.gif               # Animated background
├── User Guide.txt         # Documentation
└── voices.txt             # List of supported TTS voices

🖼️ Screenshots

(Add your screenshots here later)
Example placeholder:

<p align="center"> <img src="https://i.imgur.com/g6u3G8w.png" width="600px"> </p>
🔥 Future Enhancements

Wake-word activation (“Hey Waifu”)

Custom training data

Built-in memory system

GPT-style chat history

Anime avatar lip-sync

Web version deployable on Netlify

🌟 Author

👩‍💻 Harini A
🎓 B.Tech IT | M.Kumarasamy College of Engineering
📍 Dindigul, Tamil Nadu, India

🌐 Portfolio: https://harinii2415.github.io

💼 LinkedIn: https://www.linkedin.com/in/harini-a-9a014925a/

🐙 GitHub: https://github.com/HARINII2415

💖 Final Note

This project started as a small inspiration from an Instagram reel —
and grew into a full-fledged anime-style AI assistant.

“Anything you imagine can become reality if you start building.” 💫
