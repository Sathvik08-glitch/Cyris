from voice import speak
from memory import load_memory, save_memory
from logger import log

def handle_memory(command):

    if "what do you remember" in command:

        memory = load_memory()

        if "facts" in memory and memory["facts"]:
            memories = ", ".join(memory["facts"])
            log("Memory Requested")
            speak(f"I remember the following. {memories}")
        else:
            speak("I do not remember anything yet.")

        return True


    elif "remember" in command:

        fact = command.replace("remember", "").strip()

        if not fact:
            speak("What would you like me to remember?")
            return True

        memory = load_memory()

        if "facts" not in memory:
            memory["facts"] = []

        memory["facts"].append(fact)

        save_memory(memory)

        log(f"Remembered: {fact}")
        
        speak("I will remember that.")

        return True

    return False