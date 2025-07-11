# 🧠 Klassy – An AI-Powered School Receptionist Bot

**Klassy** is an intelligent voice assistant designed specifically for schools in India. Built with offline and online capabilities, it responds to voice commands like "What's the weather?" or "Tell me the time", and can answer general knowledge or school-related queries using Groq's LLM.

---

## 🎯 Project Goals

- Act as a virtual school receptionist for **Delhi Public School** and other Indian institutions.
- Support **Hindi + English (Hinglish)** voice queries.
- Work on **low-resource systems** like a Raspberry Pi with optional internet access.
- Respond contextually with memory and local awareness (e.g., time in Lucknow, INR, IST).

---

⚙️ How It Works
Here's a simplified breakdown of how Klassy responds to voice queries:

Wake Word Detection

Listens continuously for the wake word: "Klassy"

Starts active listening once detected

Speech-to-Text (STT)

Captures your spoken query using a microphone

Converts audio to text using the offline Vosk model

Intent Handling

Determines whether the query is about:

Time or weather (handled locally)

General/school queries (handled via Groq's LLM)

Exit commands like “bye” or “shutdown”

LLM or Local Processing

If weather/time: responds locally with city-aware logic

Else: sends the query to Groq's LLaMA model for a smart response

Memory & Context

Recent queries are stored temporarily in memory (JSON)

Helps make answers more contextual and conversational

Text-to-Speech (TTS)

Converts the bot’s text response back into speech

Uses pyttsx3 to speak out the answer naturally

Ready for Next Query

Returns to listening mode after answering

---

## ✨ Features

- ✅ **Wake Word Activation** – Start conversation with "Klassy"
- 🎙️ **Speech-to-Text** using Vosk (offline-capable)
- 🗣️ **Text-to-Speech** via pyttsx3 (local voice)
- 🌤️ **Weather reports** using OpenWeather API
- 🕒 **Time & Date** – Answers based on city or default (IST)
- 💬 **Groq-powered LLM** – Answers school-related and general queries
- 🧠 **Memory** – Keeps short-term history for smarter follow-ups
- 🔒 **Inappropriate query blocking** – Avoids responding to unsafe input

---

## 🛠️ Requirements

Install all dependencies with:

```bash
pip install -r requirements.txt
Python version: 3.10+

📁 Project Structure
School_assistant_bot/
│
├── main.py                    # Main launcher script
├── config.py                  # Configuration file (API keys, model paths)
├── stt.py                     # Speech-to-text using Vosk
├── tts.py                     # Text-to-speech
├── wake_word.py               # Detects wake word
├── weather.py                 # Weather query handler
├── time_handler.py            # Handles time/date responses
├── groq_engine.py             # Sends queries to Groq LLM
├── memory.py                  # Chat history loader/saver
├── model/                     # (Includes small EN-US Vosk model)
├── chat_history.json          # Runtime memory file
├── requirements.txt           # All required Python packages
└── .gitignore                 # Ensures large files aren’t pushed
🔑 API Keys & Setup
In config.py, the following environment variables should be set locally:

GROQ_API_KEY – Get one here

OPENWEATHER_API_KEY – Get one here

You can set them via a .env file (if using python-dotenv) or through your system environment variables.

🚀 Running the Assistant
Once dependencies and API keys are set, run:

python main.py
Then say:
"Klassy, what’s the weather in Lucknow?"
or
"Klassy, aaj ka time kya hai?"

🔒 Important Notes
The Vosk small EN-US model is included. For Hindi or Indian English, download larger Vosk models.

Avoid pushing large models to GitHub — use .gitignore.

🤖 Future Plans
Add camera-based attendance & face recognition

GUI-based dashboard for teachers/staff

Integration with school timetable / announcements

📍 Author
Abheesht Mishra – AI Intern, 2025

Developed for Delhi Public School as part of a AI ENGINEER internship.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.


