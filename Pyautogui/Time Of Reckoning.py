import pyautogui
import keyboard
import time

time.sleep(3)
while not keyboard.is_pressed('`'):
    text_to_type = "Yap yap yap"
    for letter in text_to_type:
        pyautogui.typewrite(letter)
    time.sleep(1)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("delete")