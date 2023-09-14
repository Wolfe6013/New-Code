import random

Again = 'Y'
YourMoney = int(input('How much money do you have? $'))
MoneyOwned = YourMoney
Win = 2
while Again == 'Y':
    ValidBetAmount = 1
    if Win == 1:
        MoneyOwned = MoneyOwned+BetAmount
    if Win == 0:
        MoneyOwned = MoneyOwned-BetAmount
    if MoneyOwned == 0:
        print("Poor. You can't play anymore, sorry.")
        break
    bet = input("What bet? ")
    while ValidBetAmount == 1:
        print("you have $",MoneyOwned)
        BetAmount = int(input("Money bet: $"))
        if BetAmount > MoneyOwned:
            print(BetAmount,"is larger than your total money (",MoneyOwned,")")
        else:
            ValidBetAmount = 0
    Win = 0
    Roll = random.randint(0,36)
    if Roll > 0 and Roll < 11:
        if (Roll % 2) == 0:
            Colour = 'black'
        else:
            Colour = 'red'
    if Roll > 10 and Roll < 19:
        if (Roll % 2) == 0:
            Colour = 'red'
        else:
            Colour = 'black'
    if Roll > 18 and Roll < 29:
        if (Roll % 2) == 0:
            Colour = 'black'
        else:
            Colour = 'red'
    if Roll > 28:
        if (Roll % 2) == 0:
            Colour = 'red'
        else:
            Colour = 'black'
    if Roll == 0:
        Colour = 'Green'
    print(Roll)
    print("The ball landed in",Roll,"and the colour is",Colour)
    if bet == '1-18':
        if Roll > 0 and Roll < 19:
            print('You win!')
            Win = 1
        else:
            print('You lose!')
    if bet == '19-36':
        if Roll > 18:
            print('You win!')
            Win = 1
        else:
            print('You lose!')
    if bet == 'Red':
        if Colour == 'red':
            print('You win!')
            Win = 1
        else:
            print('You lose!')
    if bet == 'Black':
        if Colour == 'black':
            print('You win!')
            Win = 1
        else:
            print('You lose!')
    if bet == 'Even':
        if (Roll % 2) == 0:
            print('You win!')
            Win = 1
        else:
            print('You lose!')
    if bet == 'Odd':
        if (Roll % 2) == 1:
            print('You win!')
            Win = 1
        else:
            print('You lose!')
    if bet == '1' or bet == '2' or bet == '3' or bet == '4' or bet == '5' or bet == '6' or bet == '7' or bet == '8' or bet == '9' or bet == '10' or bet == '11' or bet == '12' or bet == '13' or bet == '14' or bet == '15' or bet == '16' or bet == '17' or bet == '18' or bet == '19' or bet == '20' or bet == '21' or bet == '22' or bet == '23' or bet == '24' or bet == '25' or bet == '26' or bet == '27' or bet == '28' or bet == '29' or bet == '30' or bet == '31' or bet == '32' or bet == '33' or bet == '34' or bet == '35' or bet == '36':
        if int(bet) == Roll:
            print('You win!')
            Win = 1
        else:
            print('You lose!')