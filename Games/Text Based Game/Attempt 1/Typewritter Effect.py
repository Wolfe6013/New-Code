import time, sys

text = "Hello Adventurer, we have been waiting for you for a long time. Please save our village. Here, take this to help you. You get a sword! +5 Mana, +5 ATK. Please, defeat the witch!"

for char in text:
    print(char,end="")
    sys.stdout.flush()
    time.sleep(0.05)