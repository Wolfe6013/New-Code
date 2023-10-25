import pyautogui
from PIL import ImageGrab
import keyboard
import numpy as np
import time

time.sleep(1)
while not keyboard.is_pressed('q'):
    for x in range(374,1689):
        for y in range(266,1039):
            if x % 100 == 0:
                if y % 100 == 0:
                    pyautogui.click(x,y)