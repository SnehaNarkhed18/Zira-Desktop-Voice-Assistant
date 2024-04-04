#Code of Desktop Voice Assistant

import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import pyjokes
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Zira. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if _name_ == "_main_":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        
        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open presentation' in query:
            codePath = "C://Users//Dell//Desktop//Desktop Voice Assistant"
            os.startfile(codePath)

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()


