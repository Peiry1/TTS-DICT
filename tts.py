import pyttsx3

class TTS:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text):
        """发音"""
        self.engine.say(text)
        self.engine.runAndWait()

class OnlineVoice:
    def __init__(self):
        pass
