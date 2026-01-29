import random

Answers = ["No","Yes","Maybe","Definitely Not","Definitely"]

while True:
    H = input('What do you wish to ask the 8-Ball? ')
    if H == 'is Dejan a bad person?':
        print('He is definitely a bad person')
    else:
        RandAnswer = random.choice(Answers)
        print(RandAnswer)