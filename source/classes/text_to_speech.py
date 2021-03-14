import speech_recognition as sr


class VoiceRecognitionModule:
    def __init__(self, key=None):
        self.key = key
        self.r = sr.Recognizer()

    def recognize(self):
        with sr.Microphone() as source:
            print("Speak Anything : ")
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio, key=self.key, language="es")
                return text
            except:
                return None
