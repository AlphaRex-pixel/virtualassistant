import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyautogui
import psutil

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!")
    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    elif hour>=18 and hour<=24:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("Friday at your service. How I can help you?")
    speak("I can provide the following services")
    print("1.Time")
    print("2.Date")
    print("3.Offline")
    print("4.Wikipedia")
    print("5.Search in Chrome")
    print("6.Log Out")
    print("7.Shutdown")
    print("8.Restart")
    print("9.Remember Information")
    print("10.Retrieve any saved information")
    print("11.Screenshot")
    print("12.Battery level")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language = "en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please....")

        return "None"

    return query

def screenshot():
    img = pyautogui.screenshot()
    img.save()

def cpu():
    usage = str(psutil.cpu_percent)
    speak("CPU is at "+usage)

    battery = psutil.sensors_battery()
    speak("battery is at ")
    speak(battery.percent)

if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Listening....")
            speak("What do you need information about")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2) 
            speak(result)
        elif "search in chrome" in query:
            speak("What Should i search?")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+ ".com")
        elif "log out" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "remember that" in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said me to remember"+ data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember = open("data.txt", "r")
            speak("You said me to remember that"+ remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("Done!!")
        elif "battery" in query:
            cpu()                








