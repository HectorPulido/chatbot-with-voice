"""
source/classes/text_to_speech.py: Module to convert text to speech.
"""

from sys import platform

if platform == "darwin":
    from os import system
else:
    import pyttsx3


class SpeechModule:
    def __init__(self, voice="Mónica", volume=1, rate=125):
        self.voice = voice

        if platform == "darwin":
            return
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volume", volume)

        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[voice].id)

    def talk(self, text):
        """
        Function to convert text to speech.
        """
        if platform == "darwin":
            system(f'say -v "{self.voice}" {text}')
            return
        self.engine.say(text)
        self.engine.runAndWait()
