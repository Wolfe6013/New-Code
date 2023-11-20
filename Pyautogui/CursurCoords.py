import os, random, time, sys, pyautogui, keyboard

def TakeCoords():
    x, y = pyautogui.position()
    print(f"Current Cursor Coordinates: x={x}, y={y}")
    time.sleep(0.1)

keyboard.add_hotkey('c', TakeCoords)

keyboard.wait()