import json

def load_memory():
    try:
        with open("memory.json", "r") as file:
            return json.load(file)
    except:
        return {}
    
def save_memory(memory):
    with open("memory.json", "w") as file:
        json.dump(memory, file, indent = 4)
        