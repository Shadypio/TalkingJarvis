import pyttsx3
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 150  # specifies the speed of the voice
engine.setProperty('rate', newVoiceRate)

# starts the talk
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# tells the current time
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

# tells the current date
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("La data di oggi è")
    speak(day)
    speak(month)
    speak(year)

speak("Buongiorno a tutti")
date()