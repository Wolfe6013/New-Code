import random

Answers = ["No","Yes","Maybe","Definitely Not","Definitely"]

while True:
    H = input('What do you wish to ask the 8-Ball? ')
    RandAnswer = random.choice(Answers)
    print(RandAnswer)