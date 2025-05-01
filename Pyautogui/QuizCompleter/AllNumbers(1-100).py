import pyautogui
import keyboard
import time

#https://www.jetpunk.com/quizzes/fast-typing-to-hundred-quiz
time.sleep(3)
for x, y in enumerate(range(100)):
    pyautogui.typewrite(f"{y+1}")