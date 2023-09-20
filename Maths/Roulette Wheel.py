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
    bet = input("Do you want to bet on '1-18' or '19-36' or 'Red' or 'Black' or 'Even' or 'Odd'? ")
    while ValidBetAmount == 1:
        BetAmount = int(input(f"Amount you are betting (you have ${MoneyOwned}): $"))
        if BetAmount > MoneyOwned:
            print(f"{BetAmount} is larger than your total money ({MoneyOwned})")
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
    print(f'{Roll}')
    print(f'The ball landed in {Roll} and the colour is {Colour}')
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
    if MoneyOwned == 0:
        print("Poor. /nYou can't play anymore, sorry.")
        Again = 'N'
    else:
        Again = input('Play Again? (Y/N) ')