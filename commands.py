from voice import speak
from logger import log
from apps import (

    open_brave,
    open_chrome,
    open_notepad,
    open_calculator,
    open_vscode,
    open_spotify,

)

from workflow import coding_mode
from system import (

    get_battery,
    get_ram,
    get_cpu,
    get_storage,
    
)

import datetime


def handle_command(command):

    if "hello" in command:
        log("Greeting Requested")
        speak("Hello, I am Cyris.")
        return True

    elif "time" in command:
        log("Time Requested")
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")
        return True

    elif "open brave" in command:
        log("Open Brave")
        speak("Opening Brave")
        open_brave()
        return True

    elif "open chrome" in command:
        log("Open Chrome")
        speak("Opening Chrome")
        open_chrome()
        return True

    elif "open calculator" in command:
        log("Open Calculator")
        speak("Opening Calculator")
        open_calculator()
        return True

    elif "open notepad" in command:
        log("Open Notepad")
        speak("Opening Notepad")
        open_notepad()
        return True

    elif "open vscode" in command:
        log("Open VSCode")
        speak("Opening Visual Studio Code")
        open_vscode()
        return True
    
    elif "open spotify" in command:
        log("Open Spotify")
        speak("Opening Spotify")
        open_spotify()
        return True

    elif "battery" in command:
        log("Battery Requested")
        speak(get_battery())
        return True

    elif "ram" in command:
        log("RAM Requested")
        speak(get_ram())
        return True

    elif "cpu" in command:
        log("CPU Requested")
        speak(get_cpu())
        return True

    elif "storage" in command:
        log("Storage Requested")
        speak(get_storage())
        return True

    return False
