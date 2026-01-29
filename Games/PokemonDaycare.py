import keyboard, time

time.sleep(3)
for x in range(300):
    keyboard.press("right")
    time.sleep(0.5)
    keyboard.press("down")
    time.sleep(0.5)