# Trial_AI_Assistant# 

🧠 Klassy – An AI-Powered School Receptionist Bot

**Klassy** is an intelligent bilingual voice assistant designed specifically for schools in India. Built with offline and online capabilities, it responds to voice commands like "What's the weather?" or "Tell me the time", and can answer general knowledge or school-related queries using Groq's LLM.

---

## 🎯 Project Goals

- Act as a virtual school receptionist for **Delhi Public School** and other Indian institutions.
- Support **Hindi + English (Hinglish)** voice queries.
- Work on **low-resource systems** like a Raspberry Pi with optional internet access.
- Respond contextually with memory and local awareness (e.g., time in Lucknow, INR, IST).

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
graphql
Copy
Edit
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

bash
Copy
Edit
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
Varnan – AI Intern, 2025

Developed for Delhi Public School as part of a voice interface research internship.

📄 License
MIT – Feel free to use, modify, and contribute!