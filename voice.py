import speech_recognition as sr
import time

# 🔊 NEW VOICE SYSTEM (stable)
from gtts import gTTS
import pygame
import os

__all__ = ["speak", "listen"]

pygame.mixer.init()


def speak(text):
    print("Cyris:", text)

    if not text.strip():
        return

    filename = "voice.mp3"
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.unload()
    os.remove(filename)


# 🎤 Listen function (your whisper mode kept)
def listen():
    r = sr.Recognizer()

    r.energy_threshold = 100
    r.dynamic_energy_threshold = True
    r.pause_threshold = 1.2

    with sr.Microphone() as source:
        print("Listening (whisper mode)...")
        r.adjust_for_ambient_noise(source, duration=2)

        try:
            audio = r.listen(source, timeout=7, phrase_time_limit=8)
            command = r.recognize_google(audio, language='en-IN')
            print("You:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            return ""

        except sr.UnknownValueError:
            print("Didn't catch that")
            return ""

        except Exception as e:
            print("Error:", str(e))
            return ""
        
        