import pyautogui
import time

def Coords():
    x, y = pyautogui.position()
    print(f"Current Cursor Coordinates: x={x}, y={y}")

keyboard.add_hotkey('space', Coords)