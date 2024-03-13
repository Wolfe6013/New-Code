import datetime,os

users = [["Player1","Password",0,12,3,2024],
    ["Player2","12345",4,13,3,24],
    ["Player3","PaSsWoRd",9,1,3,2024]]

def clear():
    os.system("cls")

def save():
    f = open("EverydayLogin.txt","w")
    for user in users:
        for variable in user:
            f.write(f"{variable}")
            if variable != user[-1]:
                f.write(f";")
        f.write("\n")
    f.close()

def load():
    try:
        f = open("save.txt","r")
        load_list = f.readlines()
        corrupt = False
        for user in load_list:
            if len(user) != 6:
                corrupt = True
        if not corrupt:
            username = load_list[0][:-1]
            password = int(load_list[1][:-1])
            score = int(load_list[2][:-1])
            day = int(load_list[3][:-1])
            month = int(load_list[4][:-1])
            year = int(load_list[5][:-1])
            clear()
            print(f"│WELCOME BACK {username}!")
            input(f"│<")
        else:
            print(f"│CORRUPT SAVE FILE!")
            input(f"│<")
    except OSError:
        print(f"│NO LOADABLE SAVE FILE!")
        input(f"│<")