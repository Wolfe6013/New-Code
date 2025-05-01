import pyautogui
import keyboard
import time

time.sleep(3)
for x, y in enumerate(range(100)):
    pyautogui.press("delete")
    pyautogui.hotkey("ctrl", "right")
    pyautogui.press("delete")
    time.sleep(0.1)