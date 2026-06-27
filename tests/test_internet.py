from internet_commands import handle_internet

while True:
    command = input("Command: ").lower()

    if command == "exit":
        break

    handled = handle_internet(command)

    if not handled:
        print("Unknown command")