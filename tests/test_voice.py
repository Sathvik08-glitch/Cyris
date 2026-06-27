from voice import speak, listen

print("========== VOICE TEST ==========\n")

# Test Text-to-Speech
print("Testing Speak...")
speak("Hello! Voice module test successful.")

# Test Speech Recognition
print("\nTesting Listen...")
command = listen()

print("\nRecognized:", command)