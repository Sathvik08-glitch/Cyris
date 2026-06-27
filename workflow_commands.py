from voice import speak, listen

from workflow import coding_mode

from apps import (
    open_chatgpt,
    open_claude,
    open_antigravity
)

def handle_workflow(command):

    if "coding mode" not in command:
        return False

    speak("Activating coding mode")

    coding_mode()

    speak("Would you like ChatGPT, Claude, or Antigravity?")

    ai_choice = ""

    for _ in range(3):

        ai_choice = listen()

        if ai_choice:
            ai_choice = ai_choice.lower().strip()
            break

    if not ai_choice:
        speak("I didn't catch that.")
        return True

    if "chatgpt" in ai_choice or "chat gpt" in ai_choice:
        speak("Opening ChatGPT")
        open_chatgpt()

    elif "claude" in ai_choice or "cloud" in ai_choice:
        speak("Opening Claude")
        open_claude()

    elif "antigravity" in ai_choice or "anti gravity" in ai_choice:
        speak("Opening Antigravity")
        open_antigravity()

    else:
        speak("No AI selected")

    return True