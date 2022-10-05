import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

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
def wishMe():
    speak("Bentornato!")
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

if __name__ == "__main__":

    wishMe()

    while True:
        query = takeCommand().lower()
        print(query)

        if "data" in query:
            date()
        elif "ore" in query or "ora" in query:
            time()
        elif "off-line" in query:
            quit()
        elif "wikipedia" in query:
            wikipedia.set_lang('it')
            speak("Sto cercando...")
            query=query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
