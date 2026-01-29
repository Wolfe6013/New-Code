import pyautogui
import keyboard
import time
done = 0
time.sleep(3)
while not keyboard.is_pressed('`'):
    text_to_type = "I HATE YOU"
    pyautogui.write(text_to_type)
    pyautogui.keyDown('shift')
    pyautogui.press("enter")
    pyautogui.keyUp('shift')
    done += 1

print(done)