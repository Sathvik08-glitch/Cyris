import datetime
from voice import speak

def startup():

    hour = datetime.datetime.now().hour

    if hour < 12:
        greeting = "Good Morning"

    elif hour < 18:
        greeting = "Good Afternoon"

    else:
        greeting = "Good Evening"

    speak(f"{greeting} Sir.")
    speak("All systems are online.")
    speak("How may I assist you today?")