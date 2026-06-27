import json

with open("config.json", "r") as file:
    config = json.load(file)

ASSISTANT_NAME = config["assistant_name"]
WAKE_WORDS = config["wake_words"]
VERSION = config["version"]