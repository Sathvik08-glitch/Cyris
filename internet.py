import webbrowser
import urllib.parse


def search_google(query):
    query = urllib.parse.quote(query)
    webbrowser.open(f"https://www.google.com/search?q={query}")


def search_youtube(query):
    query = urllib.parse.quote(query)
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")


def search_github(query):
    query = urllib.parse.quote(query)
    webbrowser.open(f"https://github.com/search?q={query}")