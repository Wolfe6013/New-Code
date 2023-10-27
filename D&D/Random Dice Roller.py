import random
import time

while True:
    dice = int(input("How many sides are on the dice? "))
    num = random.randint(1,dice)
    print("You got",num,)