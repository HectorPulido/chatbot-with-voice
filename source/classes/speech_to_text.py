"""
source/classes/speech_to_text.py: Module to recognize speech from microphone.
"""
import speech_recognition as sr


class VoiceRecognitionModule:
    def __init__(self, language="es"):
        self.language = language
        self.recognizer = sr.Recognizer()

    def recognize(self):
        """
        Function to recognize speech from microphone.
        """
        with sr.Microphone() as source:
            print("Speak Anything : ")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_whisper(audio, language=self.language)
                return text
            except Exception as exception:
                return f"Exception occurred: {exception}"
