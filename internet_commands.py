from voice import speak
from internet import (
    search_google,
    search_youtube,
    search_github
)

def extract_query(command, keyword):
    return command.replace(keyword, "", 1).strip()


def handle_internet(command):

    if command.startswith("search youtube"):
        query = extract_query(command, "search youtube")

        if query:
            speak(f"Searching YouTube for {query}")
            search_youtube(query)

        return True

    elif command.startswith("search github"):
        query = extract_query(command, "search github")

        if query:
            speak(f"Searching GitHub for {query}")
            search_github(query)

        return True

    elif command.startswith("search google"):
        query = extract_query(command, "search google")

        if query:
            speak(f"Searching Google for {query}")
            search_google(query)

        return True

    elif command.startswith("search "):
        query = extract_query(command, "search")

        if query:
            speak(f"Searching Google for {query}")
            search_google(query)

        return True

    return False