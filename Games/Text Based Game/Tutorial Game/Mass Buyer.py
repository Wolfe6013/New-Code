import pyautogui
import keyboard
import time

elixOrPot = input("ELIX OR POT?")
num = int(input(f"HOW MANY {elixOrPot}S DO YOU WANT?"))

time.sleep(3)

if elixOrPot == "ELIX":
    for x in range(num):
        pyautogui.typewrite('5')
        pyautogui.press('enter')
        pyautogui.typewrite('4')
        pyautogui.press('enter')
        pyautogui.typewrite('40')
        pyautogui.press('enter')

if elixOrPot == "POT":
    for x in range(num):
        pyautogui.typewrite('5')
        pyautogui.press('enter')
        pyautogui.typewrite('3')
        pyautogui.press('enter')
        pyautogui.typewrite('15')
        pyautogui.press('enter')
        time.sleep(0.05)