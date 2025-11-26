import asyncio
import edge_tts
import playsound
import speech_recognition as sr
import webbrowser
import wikipedia
import pygetwindow as gw
import pyautogui
import os
import time
import random
import tkinter as tk
from threading import Thread
from tkinter import Scrollbar, Text, END
from PIL import Image, ImageTk, ImageSequence
import sys
import re
import datetime
from responses4u import responses

# ==========================================================
#  RESOURCE PATH (PyInstaller safe)
# ==========================================================
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

listener = sr.Recognizer()

# ==========================================================
#  FAST, CLEAR JAPANESE VOICE FUNCTION
# ==========================================================
async def speak(text, tries=2):
    """Quick and clear Japanese anime-style speech"""
    print("AI:", text)
    clean_text = text
    clean_text = re.sub(r"<s>|<s>|<S>|</S>", "", clean_text)  # remove <s> tags
    clean_text = re.sub(r"\[OUT\]", "", clean_text)            # remove [OUT]
    clean_text = re.sub(r"\s+s\s*$", "", clean_text.strip())   # remove trailing 's'
    clean_text = re.sub(r"^\s*s\s+", "", clean_text.strip())   # remove starting 's'
    clean_text = clean_text.strip()

    filename = f"voice_{int(time.time()*1000)}.mp3"

    for attempt in range(tries):
        try:
            communicate = edge_tts.Communicate(
                text,
                voice="ja-JP-NanamiNeural",   # cute anime tone
                rate="+5%",                   # normal speed (clear)
                pitch="+30Hz"                 # lively tone
            )
            await communicate.save(filename)
            playsound.playsound(filename, block=False)  # async playback
            break
        except Exception as e:
            print(f"TTS error (try {attempt+1}):", e)
            await asyncio.sleep(1)
    try:
        if os.path.exists(filename):
            os.remove(filename)
    except PermissionError:
        pass

# ==========================================================
#  VOICE INPUT
# ==========================================================
def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source, phrase_time_limit=4)
    try:
        command = listener.recognize_google(audio).lower()
        print("You:", command)
        return command
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return "network error"

# ==========================================================
#  WEBSITE OPEN
# ==========================================================
async def open_any_website(command):
    known_sites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "instagram": "https://www.instagram.com",
        "chatgpt": "https://chat.openai.com",
        "github": "https://github.com",
        "spotify": "https://open.spotify.com"
    }
    for name, url in known_sites.items():
        if name in command:
            await speak(f"Opening {name}")
            await asyncio.to_thread(webbrowser.open, url)
            return True

    if "open" in command:
        site = command.split("open")[-1].strip().replace(" ", "")
        await speak(f"Trying to open {site}")
        await asyncio.to_thread(webbrowser.open, f"https://www.{site}.com")
        return True
    return False

# ==========================================================
#  CLOSE APPLICATION
# ==========================================================
async def close_application(command):
    keyword = command.replace("close", "").replace("app", "").strip().lower()
    for window in gw.getWindowsWithTitle(''):
        if keyword in window.title.lower():
            try:
                window.close()
                await speak(f"Closed {keyword}")
                return
            except:
                pass
    await speak(f"No window found with {keyword}")

# ==========================================================
#  SEARCH COMMAND
# ==========================================================
async def search_anything(command):
    query = command.lower().replace("search", "").replace("for", "").strip()
    if "youtube" in command:
        query = query.replace("on youtube", "").strip()
        await speak(f"Searching YouTube for {query}")
        await asyncio.to_thread(webbrowser.open, f"https://www.youtube.com/results?search_query={query}")
    elif "chat gpt" in command:
        query = query.replace("on chat gpt", "").strip()
        await speak(f"Searching ChatGPT for {query}")
        await asyncio.to_thread(webbrowser.open, f"https://chat.openai.com/?q={query}")
    else:
        query = query.replace("on google", "").strip()
        await speak(f"Searching Google for {query}")
        await asyncio.to_thread(webbrowser.open, f"https://www.google.com/search?q={query}")

# ==========================================================
#  REPEAT / SAY
# ==========================================================
async def repeat_after_me(command):
    to_repeat = ""
    if "repeat after me" in command:
        to_repeat = command.split("repeat after me", 1)[-1].strip()
    elif "say" in command:
        to_repeat = command.split("say", 1)[-1].strip()
    if to_repeat:
        await speak(to_repeat)
        return True
    return False

# ==========================================================
#  WIKIPEDIA FUNCTIONS
# ==========================================================
async def tell_about_topic(command):
    triggers = ["do you know about", "tell me about", "who is", "what do you know about"]
    for phrase in triggers:
        if phrase in command:
            topic = command
            for t in triggers:
                topic = topic.replace(t, "")
            topic = topic.strip()
            try:
                info = wikipedia.summary(topic, sentences=2)
                await speak(info)
            except Exception:
                await speak(f"I couldn't find info about {topic}")
            return True
    return False

async def explain_meaning(command):
    triggers = ["what is", "define", "explain", "meaning of"]
    for t in triggers:
        if t in command:
            topic = command.replace(t, "").strip()
            try:
                info = wikipedia.summary(topic, sentences=2)
                await speak(info)
            except Exception:
                await speak(f"I couldn't find meaning of {topic}")
            return True
    return False

# ==========================================================
#  TIMER
# ==========================================================
async def set_timer(command):
    pattern = r"timer for (\d+)\s*(seconds|second|minutes|minute)"
    match = re.search(pattern, command)
    if match:
        value = int(match.group(1))
        unit = match.group(2)
        sec = value if "second" in unit else value * 60
        await speak(f"Timer set for {value} {unit}")
        await asyncio.sleep(sec)
        await speak("Time's up!")
    else:
        await speak("I couldn't understand the timer duration.")

# ==========================================================
#  GREETING
# ==========================================================
async def time_based_greeting():
    h = datetime.datetime.now().hour
    if 5 <= h < 12:
        await speak("Ohayo! Good morning senpai!")
    elif 12 <= h < 17:
        await speak("Konnichiwa! Good afternoon!")
    elif 17 <= h < 22:
        await speak("Konbanwa! Good evening!")
    else:
        await speak("Yoru desu ne... It's quite late!")

# ==========================================================
#  SMALL TALK
# ==========================================================
async def handle_small_talk(command):
    for key in responses:
        if key in command:
            await speak(random.choice(responses[key]))
            return True
    return False

# ==========================================================
#  SPOTIFY PLAY
# ==========================================================
async def play_song_on_spotify(command):
    if "spotify" in command:
        song = command.replace("play", "").replace("on spotify", "").strip()
        await speak(f"Searching {song} on Spotify")
        await asyncio.to_thread(webbrowser.open, f"https://open.spotify.com/search/{song}")
        await asyncio.sleep(5)
        pyautogui.press('tab', presses=5, interval=0.3)
        pyautogui.press('enter')
        await asyncio.sleep(1)
        pyautogui.press('space')

# ==========================================================
#  MAIN GUI CLASS
# ==========================================================
class AssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("VIONEX AI - Anime Voice")
        self.root.geometry("800x700")
        self.root.configure(bg="black")
        self.root.resizable(False, False)
        self.root.wm_attributes("-topmost", True)

        # Background Animation
        self.canvas = tk.Canvas(self.root, width=800, height=700, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        gif = Image.open(resource_path("elf2.gif"))
        framesize = (800, 600)
        self.frames = [ImageTk.PhotoImage(img.resize(framesize, Image.LANCZOS).convert('RGBA'))
                       for img in ImageSequence.Iterator(gif)]
        self.index = 0
        self.bg = self.canvas.create_image(0, 0, anchor='nw', image=self.frames[0])
        self.animate()

        # Chat log
        self.chat = Text(self.root, bg="#000", fg="skyblue", font=("Consolas", 10), wrap='word', bd=0)
        self.chat.place(x=0, y=600, width=800, height=100)
        self.chat.insert(END, "[System] Type below or press F2 to speak.\n")
        self.chat.config(state=tk.DISABLED)

        self.entry = tk.Entry(self.root, font=("Segoe UI", 13), bg="#1a1a1a", fg="white", bd=3)
        self.entry.place(x=20, y=670, width=700, height=30)
        self.entry.bind("<Return>", self.send_text)
        tk.Button(self.root, text="Send", command=self.send_text, bg="#222", fg="white").place(x=730, y=670, width=50, height=30)

        self.root.bind("<F2>", lambda e: Thread(target=self.listen_voice).start())
        Thread(target=lambda: asyncio.run(time_based_greeting())).start()

    def animate(self):
        self.canvas.itemconfig(self.bg, image=self.frames[self.index])
        self.index = (self.index + 1) % len(self.frames)
        self.root.after(100, self.animate)

    def add_text(self, text):
        self.chat.config(state=tk.NORMAL)
        self.chat.insert(END, text + "\n")
        self.chat.config(state=tk.DISABLED)
        self.chat.see(END)

    def send_text(self, event=None):
        txt = self.entry.get()
        self.entry.delete(0, END)
        if txt:
            self.add_text("You: " + txt)
            Thread(target=lambda: asyncio.run(self.handle_command(txt))).start()

    def listen_voice(self):
        self.add_text("[System] Listening...")
        cmd = listen_command()
        if cmd:
            self.add_text("You: " + cmd)
            Thread(target=lambda: asyncio.run(self.handle_command(cmd))).start()

    async def handle_command(self, command):
        if command == "network error":
            self.add_text("[System] Network error")
            await speak("Network issue detected.")
            return

        if await handle_small_talk(command): return
        if "open" in command and await open_any_website(command): return
        if "close" in command: await close_application(command); return
        if "timer" in command: await set_timer(command); return
        if await repeat_after_me(command): return
        if "search" in command: await search_anything(command); return
        if await explain_meaning(command): return
        if await tell_about_topic(command): return
        if "spotify" in command: await play_song_on_spotify(command); return
        if "exit" in command:
            self.add_text("[System] Exiting...")
            await speak("Goodbye senpai!")
            self.root.quit()
            return

        self.add_text("AI: I didn't get that.")
        await speak("Gomen ne... I didn't understand.")

# ==========================================================
def main():
    root = tk.Tk()
    app = AssistantGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
