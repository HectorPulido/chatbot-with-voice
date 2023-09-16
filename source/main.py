"""
source/main.py: Main module to run the program.
"""

import time
from gpt4all import GPT4All
from classes import SpeechModule, VoiceRecognitionModule, Translator

CONTEXT = """You are a useful assistant
Question: {user_input}
Answer:"""
MODEL = "llama-2-7b-chat.ggmlv3.q4_K_M.bin"

brain = GPT4All(MODEL)
speech = SpeechModule()
translator = Translator()
recognition = VoiceRecognitionModule()

while True:
    text = recognition.recognize()
    if text:
        translator_text = translator.spanish_to_english(text)
        chatbot_text = brain.generate(CONTEXT.replace("user_input", translator_text))
        chatbot_text = translator.english_to_spanish(chatbot_text)
        speech.talk(chatbot_text)
    else:
        speech.talk("No te he entendido")
    time.sleep(1)
