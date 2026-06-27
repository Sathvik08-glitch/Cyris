import time

from voice import speak, listen
from brain import get_response
from startup import startup 
from commands import handle_command
from memory_commands import handle_memory
from workflow_commands import handle_workflow 
from config import WAKE_WORDS
from internet_commands import handle_internet

startup()

while True:
    command = listen()
    print("=" * 50)
    print("Raw Input: ", repr(command))
    print("=" * 50)

    if command == "":
        time.sleep(1)
        continue

    command = command.lower().strip()


    wake_detected = False

    for word in WAKE_WORDS:
        if word in command:
            command = command.replace(word, "").strip()
            wake_detected = True
            break

    if not wake_detected:
        continue

    if handle_command(command):
        continue
    
    if handle_memory(command):
        continue

    if handle_workflow(command):
        continue

    if handle_internet(command):
        continue

    response = get_response(command)

    if response:
        speak(response)

    