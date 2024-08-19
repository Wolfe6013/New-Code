import pyautogui
from PIL import ImageGrab
import numpy as np
import time

target_color = (75,219,106)
clicksDone = 0
NoClicks = 1

while True:
    screenshot = ImageGrab.grab()
    screenshot_array = np.array(screenshot)
    roi = screenshot_array[700,500]

    if np.any(np.all(roi == target_color, axis=-1)):
        pyautogui.click(700,500,button='left', clicks=NoClicks)
        clicksDone += 1
    
    if clicksDone == 5:
        clicksDone = 0