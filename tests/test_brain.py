from brain import get_response

while True:
    command = input("You: ")

    if command.lower() == "exit":
        break
    
    print("Cyris:", get_response(command))