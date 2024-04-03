import random, os

choices = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
personsBall: list = []
nameList: list = []
done = False
while not done:
    os.system("cls")
    name: str = input("Name: ")
    if name == "DONE":
        for x in personsBall:
            print(x)
        done = True
    elif name in nameList:
        for x in personsBall:
            if name in x:
                print(x)
        input()
    else:
        ball = random.choice(choices)
        choices.remove(ball)
        print(ball)
        personsBall.append(f"{name}'s ball is {ball}")
        nameList.append(name)
        input()