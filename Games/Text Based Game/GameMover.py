import keyboard

def hotkey_pressed():
    keyboard.press("enter")
    keyboard.release("enter")

def endTask():
    quit()

keyboard.add_hotkey('W', hotkey_pressed)
keyboard.add_hotkey('A', hotkey_pressed)
keyboard.add_hotkey('S', hotkey_pressed)
keyboard.add_hotkey('D', hotkey_pressed)
keyboard.add_hotkey('0', hotkey_pressed)
keyboard.add_hotkey('1', hotkey_pressed)
keyboard.add_hotkey('2', hotkey_pressed)
keyboard.add_hotkey('3', hotkey_pressed)
keyboard.add_hotkey('4', hotkey_pressed)
keyboard.add_hotkey('5', hotkey_pressed)
keyboard.add_hotkey('6', hotkey_pressed)
keyboard.add_hotkey('7', hotkey_pressed)
keyboard.add_hotkey('8', hotkey_pressed)
keyboard.add_hotkey('X', endTask)

while True:
    input(">")