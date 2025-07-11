import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Optional: Select specific voice if you want
for voice in voices:
    if "ravi" in voice.name.lower() or "male" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    print("🤖 Speaking:", text)
    engine.say(text)
    engine.runAndWait()

def stop_speaking():
    try:
        engine.stop()
    except Exception as e:
        print("⚠️ Error stopping speech:", e)
