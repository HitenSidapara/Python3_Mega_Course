import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random



engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour < 12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")
    
    speak("I am sophia sir. Please tell me how may i help you ?")


def takecommmand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query} \n")
    
    except Exception:
        print("please say again....")
        return "None"

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommmand().lower()
        if 'wikipedia' in query:
            print("Seraching wikipedia.....")
            speak("searching wikipedia......")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia ")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("youtube.com")

        elif 'open google' in query:
            webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open_new("google.com")
        elif 'play music' in query:
            music_dir = 'F://Song//mp3 hit'
            songs = os.listdir(music_dir)
            # print(songs)
            random_music = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[random_music]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(strTime)
        elif 'open chrome' in query:
            os.startfile('"C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe"')

        elif 'open python' in query:
            os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.1\\bin\\pycharm64.exe")
        elif 'open folder' in query:
            os.startfile('F:\\Software\\SP3682U\\Python')