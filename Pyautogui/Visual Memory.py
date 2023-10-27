import cv2
import numpy as np
import pyautogui
import time

# Specify the area to look for white pixels
area = ((800, 800), (1500, 1000))

while True:
    # Take a screenshot and convert it to a numpy array
    screenshot = np.array(pyautogui.screenshot())

    # Convert the numpy array to grayscale
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Look for white pixels in the specified area
    white_pixels = np.where(gray[area[0][1]:area[1][1], area[0][0]:area[1][0]] == 255)

    # If any white pixels are found, click on one of them
    if white_pixels[0].size != 0:
        # Pick a random white pixel and calculate its coordinates
        random_pixel = np.random.randint(0, white_pixels[0].size)
        x_coord = area[0][0] + white_pixels[1][random_pixel]
        y_coord = area[0][1] + white_pixels[0][random_pixel]

        # Convert the coordinates to the absolute screen position
        screen_x, screen_y = pyautogui.position()
        x_coord += screen_x - area[0][0]
        y_coord += screen_y - area[0][1]

        # Move the cursor to the selected white pixel and click
        pyautogui.moveTo(x_coord, y_coord, duration=0.25)
        pyautogui.click()

    # Wait for a while before checking for white pixels again
    time.sleep(300)