import random

Answers = ["No","Yes","Maybe","Definitely Not","Definitely"]

while True:
    H = input('What do you wish to ask the 8-Ball? ')
    if H == 'is Dejan a bad person?':
        print('Definately')
    else:
        RandAnswer = random.choice(Answers)
        print(RandAnswer)