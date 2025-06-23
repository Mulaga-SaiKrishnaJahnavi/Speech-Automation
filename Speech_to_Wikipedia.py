import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') #driver to get voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 - for male and 1 - for female
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your friend. Please tell me how may I help you")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        speak("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f"My friend you said that {query}\n")
    except Exception as e:
        print('Please say that again')
        speak('Please say that again')
        return "None"
    return query
'''
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pythonsamplepractice@gmail.com', 'Python@Sample123')
    server.sendmail('pythonsamplepractice@gmail.com', to, content)
    server.close()
'''

if __name__ == "__main__":
    wish()

    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("The term is ambiguous, please be more specific.")
                print(f"DisambiguationError: {e}")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I could not find any information on that topic.")
            except Exception as e:
                speak("Sorry, something went wrong while fetching from Wikipedia.")
                print(f"Error: {e}")
        elif 'notepad' in query:
            npath ="C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
        elif 'paint' in query:
            npath = "C:\\Windows\\System32\\mspaint.exe"
            os.startfile(npath)
        elif 'youtube' in query:
            webbrowser.open('youtube.com')
        elif 'google' in query:
            webbrowser.open('google.com')
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'linkedin' in query:
            webbrowser.open('linkedin.com')
        elif 'bye' in query:
            speak('Thank you, if need any help please execute me')
            break


