import pyautogui
import keyboard
import time

while True:
    text_to_type = input("What to type? ")
    time.sleep(1)
    pyautogui.typewrite(text_to_type)