import datetime
import time
import json
from voice import speak, listen
from memory import load_memory, save_memory
from system import get_battery, get_ram, get_cpu, get_storage
from workflow import coding_mode
from apps import (
    open_brave,
    open_chrome,
    open_notepad,
    open_calculator,
    open_vscode,
    open_chatgpt,
    open_claude,
    open_antigravity
)


# Main loop
while True:
    command = listen()

    if command == "":
        time.sleep(1)
        continue

    command = command.replace("cyrus", "cyris")
    command = command.strip()
    
    # 🎯 Wake word
    if "cyris" in command:
        command = command.replace("cyris", "").strip()
    else:
        continue

    # 💬 Commands
    if "hello" in command:
        speak("Hello, I am Cyris.")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")

    elif "open brave" in command:
        speak("Opening Brave")
        open_brave()

    elif "open chrome" in command:
        speak("Opening Chrome")
        open_chrome()

    elif "open calculator" in command:
        speak("Opening Calculator")
        open_calculator()

    elif "open notepad" in command:
        speak("Opening Notepad")
        open_notepad()

    elif "open vscode" in command:
        speak("Opening Visual Studio Code")
        open_vscode()

    elif "coding mode" in command:

        speak("Activating coding mode")

        coding_mode()

        speak("Would you like ChatGPT, Claude, or Antigravity?")

        
        ai_choice = ""
        ai_choice = ai_choice.lower().strip()

        for _ in range(3):
            ai_choice = listen()

            print("DEBUG AI CHOICE =", repr(ai_choice))

            if ai_choice:
             break
            
        if not ai_choice:
            speak("I didn't catch that. Please repeat.")

        elif ("chatgpt" in ai_choice or "chat gpt" in ai_choice or "chat jbt" in ai_choice):
            speak("Opening ChatGPT")
            open_chatgpt()

        elif "claude" in ai_choice or "cloud" in ai_choice:
            speak("Opening Claude")
            open_claude()

        elif "antigravity" in ai_choice or "anti gravoty" in ai_choice:
            speak("Opening Antigravity")
            open_antigravity()

        else:
            speak("No AI selected")

    elif "battery" in command:
        speak(get_battery())

    elif "ram" in command:
        speak(get_ram())

    elif "cpu" in command:
        speak(get_cpu())

    elif "storage" in command:
        speak(get_storage())

    elif "what do you remember" in command:

        memory = load_memory()

        if "facts" in memory and memory["facts"]:
            memories = ", ".join(memory["facts"])
            speak(f"I remember the following. {memories}")
        else:
            speak("I do not remember anything yet.")

    elif "remember" in command:

        fact = command.replace("remember", "").strip()

        if not fact:
            speak("What would you like me to remember?")
            continue 

        memory = load_memory()

        if "facts" not in memory:
            memory["facts"] = []

        memory["facts"].append(fact)

        save_memory(memory)

        speak("I will remember that.")

    elif "exit" in command:
        speak("Bye Bye!")
        break