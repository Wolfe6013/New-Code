import random

timesrun = 0
dice = int(input("How many sides on the dice? "))
mod = int(input("Any modifiers? "))
norolls = int(input("How many dice do you want to roll? "))

while timesrun < norolls:
    num = random.randint(1,dice)
    timesrun = timesrun+1
    print(num+mod)