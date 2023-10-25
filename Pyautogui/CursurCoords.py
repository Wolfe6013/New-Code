import pyautogui
import time

print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)

while True:
    x, y = pyautogui.position()
    print(f"Current Cursor Coordinates: x={x}, y={y}")
    time.sleep(1)