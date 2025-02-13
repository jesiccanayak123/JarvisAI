from time import strftime

import speech_recognition as sr
import os
import pyttsx3
from wikipedia import languages
import webbrowser
# import openai
import datetime
import smtplib
from email.mime.text import MIMEText

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        say("Good Morning!")
    elif hour >=12 and hour <18:
        say("Good Afternoon!")
    else:
        say("Good Evening!")
    say("I am Jarvis ma'am. Please tell me how can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language = "en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry from Jarvis"
def sendEmail(to,content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        # Get credentials from environment variables
        email = os.environ.get('EMAIL_ADDRESS')
        password = os.environ.get('EMAIL_PASSWORD')

        server.login(email, password)
        # Create proper email message
        msg = MIMEText(content)
        msg['Subject'] = 'Email Subject'
        msg['From'] = email
        msg['To'] = to

        server.send_message(msg)
        server.close()
        say("Email has been sent!")

    except Exception as e:
        say(f"An error occurred: {str(e)}")



if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Jarvis AI")
    wishMe()
    while True:
        print("Listening....")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"], ["stack overflow", "https://stackoverflow.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Ma'am....")
                webbrowser.open(site[1])
            if "open music" in query:
                musicPath = r"C:/Users/jesicca.nayak/Downloads/Neoni.mp3"
                os.startfile(musicPath)
            elif "the time" in query:
                strftime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Jessica the time is {strftime}")
            #For Applications
            elif "open vs code".lower() in query.lower():
                os.system(
                    r'start "" "C:/Users/jesicca.nayak/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Visual Studio Code/Visual Studio Code.lnk"')
            else:
                print("No query matched")


