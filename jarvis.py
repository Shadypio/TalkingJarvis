import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia # pip install wikipedia
import smtplib
import webbrowser as wb
import os

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

# send email
'''
No Longer Works Since 30th May, 2022
'''
def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("test@gmail.com", "pass")
    server.sendmail("test@gmail.com", to, content)
    server.close()


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
        elif "e-mail" in query or "mail" in query:
            try:
                speak("Qual è il messaggio?")
                content = takeCommand()
                to="send@gmail.com"
                sendMail(to, content)
                speak("E-mail inviata correttamente")
            except Exception as e:
                print(e)
                speak("Errore")

        elif "cerca" in query:
            speak("Cosa devo cercare?")
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        elif "log out" in query:
            os.system("shutdown - l")

        elif "spegni" in query:
            os.system("shutdown /s /t 1")

        elif "riavvia" in query:
            os.system("shutdown /r /t 1")

        elif "riproduci" in query:
            songs_dir = "#path"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif "registra" in query:
            speak("Cosa devo ricordarti?")
            data = takeCommand()
            speak("Va bene")
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "ricordami" in query:
            remember = open("data.txt", "r")
            speak(remember.read())