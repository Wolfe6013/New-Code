import pyautogui, keyboard

def Sage():
    print("Sage")
    for x in range(10):
        pyautogui.click(960,840)
        pyautogui.click(960,730)

def KJ():
    print("KJ")
    for x in range(10):
        pyautogui.click(800,840)
        pyautogui.click(960,730)

keyboard.add_hotkey('-', Sage)
keyboard.add_hotkey('=', KJ)

keyboard.wait()