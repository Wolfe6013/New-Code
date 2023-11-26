import os, random, time, sys, pyautogui, keyboard

def Code_Imports():
    keyboard.release('ctrl')
    pyautogui.write("import os, random, time, sys, pyautogui, keyboard")
    time.sleep(0.1)

def Open_Word():
    pyautogui.click(80, 1050)
    time.sleep(0.5)
    pyautogui.write("word")
    pyautogui.press("enter")

def Open_File():
    keyboard.release('ctrl')
    pyautogui.hotkey('winleft', 'e')

def Shutdown():
    pyautogui.click(20, 1048)
    pyautogui.click(20, 1000)
    pyautogui.click(20, 877)
    pyautogui.click(20, 877)

keyboard.add_hotkey('ctrl + 1', Code_Imports)
keyboard.add_hotkey('ctrl + 2', Open_Word)
keyboard.add_hotkey('ctrl + 3', Open_File)

keyboard.add_hotkey('ctrl + 9', Shutdown)

keyboard.wait()