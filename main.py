# ✅ FINALIZED main.py — Single wake word detection before interaction
import re
from wake_word import detect_klassy
from stt import listen
from tts import speak
from groq_engine import ask_question
from memory import load_history, save_history
from weather import get_weather
from time_handler import get_date_time_by_city

EXIT_COMMANDS = ["bye", "exit", "quit", "goodbye", "no thanks", "no", "no,thank you", "bye bye"]
WHO_COMMANDS = ["who are you", "what is your name", "who r you", "your name"]

WELCOME_MSG = "Hello! This is Klassy, your school receptionist. Say 'klassy' to ask me anything."

print("🤖 Klassy – your school assistant – is running...")
speak(WELCOME_MSG)

history = load_history()

while True:
    print("🛑 Waiting for wake word 'klassy'...")
    speak("Please say the wake word 'klassy' to start.")

    if detect_klassy():  # Waits until user says "klassy"
        print("✅ Wake word detected. Entering conversation mode.")
        speak("Yes, I’m listening.")

        while True:
            query = listen()
            print(f"🔍 You said: {query}")

            if query == "__RETRY__" or not query.strip():
                speak("I didn’t catch that. Say it again, please.")
                continue

            query_lower = query.lower().strip()

            if any(cmd in query_lower for cmd in EXIT_COMMANDS):
                speak("Thank you for your time. Please let me know if you need anything else.")
                break

            if any(phrase in query_lower for phrase in WHO_COMMANDS):
                speak(WELCOME_MSG)
                speak("Feel free to ask if you need any help.")
                continue

            # Local time/date/weather handling
            if re.search(r"\btime\b|\bwhat.*time\b|\btell.*time\b|\bkitne baje\b|\bkya time\b|\bsamay\b|\bबजे\b|\bसमय\b|\bclock\b", query_lower):
                response = get_date_time_by_city(query_lower, only_date=False)
                speak(response)

            elif re.search(r"\bdate\b|\btoday'?s date\b|\btoday\b|\btareekh\b|\bदिनांक\b|\bआज\b|\btoday's\b", query_lower):
                response = get_date_time_by_city(query_lower, only_date=True)
                speak(response)

            elif re.search(r"\bweather\b|\btemperature\b|\bmausam\b|\bbarish\b|\brain\b|\bcloud\b|\bhawa\b|\bमौसम\b|\bतापमान\b|\bगर्मी\b|\bसर्दी\b", query_lower):
                weather_report = get_weather(query_lower)
                speak(weather_report)

            else:
                # Groq fallback
                try:
                    answer = ask_question(query, history)
                    history.append({"role": "user", "content": query})
                    history.append({"role": "assistant", "content": answer})
                    save_history(history)
                    speak(answer)
                except Exception as e:
                    print("❌ Groq error:", e)
                    speak("Sorry, I couldn’t process that right now.")

            # Ask if more is needed
            speak("Is there anything else I can help you with?")
            followup = listen().lower()
            if any(cmd in followup for cmd in EXIT_COMMANDS) or "no" in followup:
                speak("Thank you for your time. Have a pleasant day ahead!")
                break
