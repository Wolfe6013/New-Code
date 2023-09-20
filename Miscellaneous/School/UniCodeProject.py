import sys
import random
import time

Hi = 0
CompRPS = 0
GamesDone = 0

print('The list of all functions, and how to use them:')
print('number_calculations(Number)')
print('restaurant_waiter()')
print('rps_result()')
print('population_prediction(PreyNumber,PredatorNumber,AmountofYears)')

def number_calculations(No):
    print(No/5)
    if No>=101: print('True')
    else: print('False')
    print(No % 9)
    if (No % 2) == 0: print ('True')
    else: print ('False')
    print((5-No)+(1.5*No)/3)
  
def restaurant_waiter():
    print('Hello, my name is WaiterBOT, and I will be your waiter for today.')
    time.sleep(0.5)
    name = input("What do you wish me to call you? ")
    time.sleep(0.25)
    print("Well, hello",name)
    time.sleep(0.25)
    meal = input('What meal do you want? ')
    noplates = int(input('How many do you want? '))
    print(name,'ordered',noplates,meal,)
    pay = int(input('How much (in dollars) would you like to pay per plate? '))
    print(name,'spent',pay,'dollars per meal, and ordered',noplates,'plates, to a total cost of',pay*noplates,'dollars!')
    print('Thank you for coming!')

def Question_Fetch(Response):
    AINumber = random.randint(1,3)
    AIRPS = ['Rock','Paper','Scissors']
    return str(AIRPS[AINumber-1]);

def rps_result():
    PlayerAmount = input('How Many Players (1 or 2)? ')
    if PlayerAmount == '1':
        GamesDone = 0
        while True:
            ComputerAnswer = Question_Fetch(Hi)
            OnePlayer = input("Rock, Paper, Scissors, Shoot! ")
            if OnePlayer == 'End':
                sys.exit()
            else:
                print()
                print('I picked',ComputerAnswer,'and you picked',OnePlayer)
                GamesDone = GamesDone+1
                if OnePlayer == 'Rock':
                    time.sleep(0)
                    if ComputerAnswer == 'Rock':
                        print('Draw!')
                    else:
                        time.sleep(0)
                        if ComputerAnswer == 'Paper':
                            print('Paper beats Rock')
                            print('Computer Wins!')
                        else:
                            time.sleep(0)
                            print('Rock beats Scissors')
                            print('You Win!')
                else:
                    if OnePlayer == 'Paper':
                        time.sleep(0)
                        if ComputerAnswer == 'Rock':
                            print('Paper beats Rock')
                            print('You Win!')
                        else:
                            time.sleep(0)
                            if ComputerAnswer == 'Paper':
                                print('Draw!')
                            else:
                                time.sleep(0)
                                print('Scissors beats Paper')
                                print('Computer Wins')
                    else:
                        if OnePlayer == 'Scissors':
                            time.sleep(0)
                            if ComputerAnswer == 'Rock':
                                print('Rock beats Scissors')
                                print('Computer Wins!')
                            else:
                                time.sleep(0)
                                if ComputerAnswer == 'Paper':
                                    print('Scissors beats Paper')
                                    print('You Win!')
                                else:
                                    time.sleep(0)
                                    print('Draw!')
                print()
                print('We have played',GamesDone,'game(s)')
                print()
    else:
        GamesDone = 0
        while True:
            print("Rock, Paper, Scissors, Shoot! ")
            p1input = input('Player one input: ')
            p2input = input('Player two input: ')
            if p1input == 'End':
                sys.exit()
            else:
                print()
                print('Player One picked',p1input,'and Player Two picked',p2input)
                GamesDone = GamesDone+1
                if p1input == 'Rock':
                    time.sleep(0)
                    if p2input == 'Rock':
                        print('Draw!')
                    else:
                        time.sleep(0)
                        if p2input == 'Paper':
                            print('Paper beats Rock')
                            print('Player Two Wins!')
                        else:
                            time.sleep(0)
                            print('Rock beats Scissors')
                            print('Player One Wins!')
                else:
                    if p1input == 'Paper':
                        time.sleep(0)
                        if p2input == 'Rock':
                            print('Paper beats Rock')
                            print('Player One Wins!')
                        else:
                            time.sleep(0)
                            if p2input == 'Paper':
                                print('Draw!')
                            else:
                                time.sleep(0)
                                print('Scissors beats Paper')
                                print('Player Two Wins!')
                    else:
                        if p1input == 'Scissors':
                            time.sleep(0)
                            if p2input == 'Rock':
                                print('Rock beats Scissors')
                                print('Player Two Wins!')
                            else:
                                time.sleep(0)
                                if p2input == 'Paper':
                                    print('Scissors beats Paper')
                                    print('Player One Wins!!')
                                else:
                                    time.sleep(0)
                                    print('Draw!')
                print()
                print('We have played',GamesDone,'game(s)')
                print()

def population_prediction(prey,predator,time):
    runno = 0
    while time != runno:
        firstprey = prey
        firstpredator = predator
        prey = firstprey+(0.1*firstprey)-(0.002*firstprey*firstpredator)
        predator = firstpredator+(0.0025*firstprey*firstpredator)-(0.2*firstpredator)
        runno = runno+1
        print('Estimated number of prey:',prey,'- Estimated number of predators:',predator,'- after',runno,'years')