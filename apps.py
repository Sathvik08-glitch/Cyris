import subprocess

def open_brave():
    subprocess.Popen("brave")

def open_chrome():
    subprocess.Popen("chrome")

def open_notepad():
    subprocess.Popen("notepad")

def open_calculator():
    subprocess.Popen("calc")

def open_vscode():
    subprocess.Popen(
        r"C:\Users\Sathv\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    )

def open_chatgpt():
    subprocess.Popen("ChatGPT") 

def open_antigravity():
    subprocess.Popen(
        r"C:\Users\Sathv\AppData\Local\Programs\antigravity\Antigravity.exe"
    )

def open_claude():
    subprocess.Popen(
        r"C:\Program Files\WindowsApps\Claude_1.14271.0.0_x64__pzs8sxrjxfjjc\app\Claude.exe"
    )

def open_github():
    subprocess.Popen([
        r"C:\Program Files\Google\Chrome\Application\chrome_proxy.exe",
        "--profile-directory=Default",
        "--app-id=mjoklplbddabcmpepnokjaffbmgbkkgg"
    ])

def open_spotify():
    subprocess.Popen([
        r"C:\Program Files\Google\Chrome\Application\chrome_proxy.exe",
        "--profile-directory=Default",
        "--app-id=YOUR_SPOTIFY_APP_ID"
    ])