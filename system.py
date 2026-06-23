import psutil

def get_battery():
    battery = psutil.sensors_battery()

    if battery:
        return f"Battery is at {battery.percent} percent"
    else:
        return "Battery information is unavailable"


def get_ram():
    ram = psutil.virtual_memory()

    used = round(ram.used / (1024**3), 1)
    total = round(ram.total / (1024**3), 1)

    return f"You are using {used} gigabytes out of {total} gigabytes of RAM"


def get_cpu():
    usage = psutil.cpu_percent(interval=1)

    return f"CPU usage is {usage} percent"


def get_storage():
    disk = psutil.disk_usage('/')

    free = round(disk.free / (1024**3), 1)
    total = round(disk.total / (1024**3), 1)

    return f"You have {free} gigabytes free out of {total} gigabytes"
