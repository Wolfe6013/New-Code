import pygetwindow as gw
import pyautogui
import time

open_windows = gw.getWindowsWithTitle('')
tab_count = len(open_windows)

pyautogui.click(20, 1048)
pyautogui.click(20, 1000)
pyautogui.click(20, 877)
pyautogui.click(20, 877)
if tab_count > 0:
    for window in open_windows:
        pyautogui.hotkey("alt", "f4")