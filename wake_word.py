import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import queue
import time
from config import VOSK_MODEL_PATH

WAKE_WORDS = ["klassy", "classy", "classic", "clashes"]
model = Model(VOSK_MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)
q = queue.Queue()

def callback(indata, frames, time_info, status):
    if status:
        print(f"⚠️ Stream status: {status}")
    q.put(bytes(indata))

def detect_klassy(timeout=10):
    print(f"🛑 Listening for wake word: {WAKE_WORDS}...")
    start_time = time.time()
    with sd.RawInputStream(samplerate=16000, blocksize=4000, dtype='int16',
                           channels=1, callback=callback):
        while time.time() - start_time < timeout:
            while not q.empty():
                data = q.get()
                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())
                    text = result.get("text", "").lower()
                    print(f"📝 Heard: {text}")
                    for word in WAKE_WORDS:
                        if word in text:
                            print("✅ Wake word detected!")
                            return True
    print("⏰ Wake word timeout. Listening cycle ended.")
    return False
