# config.py
import os

# 🔐 Groq API Key (fallback provided, but env var recommended)
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")

# ✅ Use a supported, powerful production model
MODEL_NAME = "llama-3.3-70b-versatile"  # Fast, multilingual, reliable

# 🗣️ Path to your Vosk STT model
VOSK_MODEL_PATH = r"model/vosk-model-en-in-0.5"
