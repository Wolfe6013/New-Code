import pyautogui
import keyboard
import time

click_locations = []  # To store the list of click locations

def add_click_location(e):
    if e.name == 's':
        x, y = pyautogui.position()
        click_locations.append((x, y))
        print(f"Added click location: x={x}, y={y}")

def clear_click_locations(e):
    if e.name == 'x':
        click_locations.clear()
        print("Cleared the list of click locations")

def perform_moves(e):
    if e.name == 'm':
        if click_locations:
            print("Performing moves at saved locations...")
            for x, y in click_locations:
                pyautogui.moveTo(x, y)
            print("All moves performed.")
        else:
            print("The list of move locations is empty. Add locations with 's' before clicking.")

def perform_clicks(e):
    if e.name == 'c':
        if click_locations:
            print("Performing clicks at saved locations...")
            for x, y in click_locations:
                pyautogui.click(x, y)
            print("All clicks performed.")
        else:
            print("The list of click locations is empty. Add locations with 's' before clicking.")

# Add keyboard event listeners
keyboard.on_press_key('s', add_click_location)
keyboard.on_press_key('x', clear_click_locations)
keyboard.on_press_key('c', perform_clicks)
keyboard.on_press_key('m', perform_moves)

print("Press 's' to add a click location, 'c' to perform clicks, and 'x' to clear the list.")
keyboard.wait('esc')  # Wait for the 'esc' key to exit the script

# Remove keyboard listeners when done
keyboard.unhook_all()