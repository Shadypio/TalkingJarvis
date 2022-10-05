import pyttsx3
import datetime
import speech_recognition as sr

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
    speak("L'orario corrente è")
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

# greetings
def wishme():
    speak("Bentornato!")
    date()
    time()
    speak("Come posso aiutarti?")

# takes a command from microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Sto ascoltando...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Sto elaborando...")
        query = r.recognize_google(audio, language = 'it-it')
        print(query)
    except Exception as e:
        print(e)
        speak("Per favore, ripeti...")

        return "None"

    return query

#  wishme()
takeCommand()