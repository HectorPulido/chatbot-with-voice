import pyttsx3


class SpeechModule:
    def __init__(self, voice=0, volume=1, rate=125):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volume", volume)

        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[voice].id)

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
