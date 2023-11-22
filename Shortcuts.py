import os, random, time, sys, pyautogui, keyboard

def Code_Imports():
    keyboard.release('ctrl')
    pyautogui.write("import os, random, time, sys, pyautogui, keyboard")
    time.sleep(0.1)

def Open_File():
    keyboard.release('ctrl')
    pyautogui.hotkey('winleft', 'e')

def Open_Word():
    pyautogui.click(80, 1050)
    time.sleep(0.5)
    pyautogui.write("word")
    pyautogui.press("enter")

def Open_Code():
    Open_File()
    time.sleep(0.5)
    pyautogui.press("f11")
    time.sleep(0.1)
    pyautogui.click(1300,135)
    pyautogui.press("enter")
    time.sleep(0.1)
    pyautogui.click(820,135)
    pyautogui.press("enter")
    time.sleep(0.1)
    
    pyautogui.click(590,115)
    pyautogui.press("enter")
    pyautogui.press("f11")

def Shutdown():
    pyautogui.click(20, 1048)
    time.sleep(0.05)
    pyautogui.click(20, 1000)
    time.sleep(0.05)
    pyautogui.click(20, 877)
    time.sleep(0.05)
    pyautogui.click(20, 877)

keyboard.add_hotkey('ctrl + 1', Code_Imports)
keyboard.add_hotkey('ctrl + 2', Open_File)
keyboard.add_hotkey('ctrl + 3', Open_Code)
keyboard.add_hotkey('ctrl + 4', Open_Word)

keyboard.add_hotkey('ctrl + 9', Shutdown)

keyboard.wait()

#