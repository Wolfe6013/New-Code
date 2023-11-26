import time, keyboard

def Deadlock():
    for x in range(100):
        pyautogui.click(800, 800)
    print("Deadlock")
    time.sleep(0.5)

def Pheonix():
    for x in range(100):
        pyautogui.click(800, 800)
    print("Pheonix")
    time.sleep(0.5)

def Viper():
    for x in range(100):
        pyautogui.click(800, 800)
    print("Viper")
    time.sleep(0.5)

def Killjoy():
    for x in range(100):
        pyautogui.click(800, 800)
    print("Killjoy")
    time.sleep(0.5)

def Sage():
    for x in range(100):
        pyautogui.click(800, 800)
    print("Sage")
    time.sleep(0.5)

def Cypher():
    for x in range(100):
        pyautogui.click(800, 800)
    print("Cypher")
    time.sleep(0.5)

def Yoru():
    for x in range(100):
        pyautogui.click(800, 800)
    print("Yoru")
    time.sleep(0.5)

keyboard.add_hotkey('ctrl + 1', Deadlock)
keyboard.add_hotkey('ctrl + 2', Pheonix)
keyboard.add_hotkey('ctrl + 3', Viper)
keyboard.add_hotkey('ctrl + 4', Killjoy)
keyboard.add_hotkey('ctrl + 5', Sage)
keyboard.add_hotkey('ctrl + 6', Cypher)

keyboard.wait()