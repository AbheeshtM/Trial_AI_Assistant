import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from config import VOSK_MODEL_PATH
import re

model = Model(VOSK_MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

def is_inappropriate(text):
    blacklist = [
        r"\b(sex|porn|nude|naked|boobs|xxx|fuck|bitch|dick|pussy|ass|horny|hot girl|hot boy)\b",
    ]
    for pattern in blacklist:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False

def listen(timeout=5):
    print("🎤 Listening... (Speak now)")
    result_text = ""

    def callback(indata, frames, time, status):
        nonlocal result_text
        if recognizer.AcceptWaveform(indata.tobytes()):
            result = json.loads(recognizer.Result())
            text = result.get("text", "")
            if text:
                result_text = text
                raise sd.CallbackStop()

    try:
        with sd.InputStream(samplerate=16000, channels=1, dtype='int16', blocksize=8000, callback=callback):
            sd.sleep(timeout * 1000)  # timeout in milliseconds
    except sd.CallbackStop:
        pass
    except Exception as e:
        print("❌ Error during listening:", e)

    result_text = result_text.strip()

    if not result_text:
        print("⚠️ No speech detected.")
        return "__RETRY__"

    if is_inappropriate(result_text):
        print("🚫 Inappropriate query blocked.")
        return "Sorry, I can't help with that."

    if len(result_text.split()) < 3:
        print("🤷 Too short or unclear input:", result_text)
        return "__RETRY__"

    return result_text
