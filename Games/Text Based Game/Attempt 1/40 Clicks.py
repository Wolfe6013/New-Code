import keyboard
import pyautogui
import time

while True:
    input()
    time.sleep(0.5)
    pyautogui.click()
    for x in range(40):
        pyautogui.press('right')
        print(x+1)