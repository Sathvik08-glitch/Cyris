import datetime


def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("activity.log", "a") as file:
        file.write(f"[{timestamp}] {message}\n")

        