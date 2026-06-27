from voice import speak
from apps import (

    open_brave,
    open_chrome,
    open_notepad,
    open_calculator,
    open_vscode,

)

from workflow import coding_mode
from system import (

    get_battery,
    get_ram,
    get_cpu,
    get_storage,
    
)

import datetime

from voice import speak
from apps import (
    open_brave,
    open_chrome,
    open_notepad,
    open_calculator,
    open_vscode,
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
        speak("Hello, I am Cyris.")
        return True

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")
        return True

    elif "open brave" in command:
        speak("Opening Brave")
        open_brave()
        return True

    elif "open chrome" in command:
        speak("Opening Chrome")
        open_chrome()
        return True

    elif "open calculator" in command:
        speak("Opening Calculator")
        open_calculator()
        return True

    elif "open notepad" in command:
        speak("Opening Notepad")
        open_notepad()
        return True

    elif "open vscode" in command:
        speak("Opening Visual Studio Code")
        open_vscode()
        return True

    elif "battery" in command:
        speak(get_battery())
        return True

    elif "ram" in command:
        speak(get_ram())
        return True

    elif "cpu" in command:
        speak(get_cpu())
        return True

    elif "storage" in command:
        speak(get_storage())
        return True

    return False
