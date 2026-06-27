def get_response(command):
    command = command.lower()
    
    if "what is java" in command:
        return "Java is an object oriented programming language."

    elif "who made you" in command:
        return "I was created by Sathvik."

    elif "who are you" in command:
        return "I am Cyris, your personal AI assistant."

    else:
        return "I don't know that yet."