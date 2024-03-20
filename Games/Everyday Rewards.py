from datetime import datetime
from EncoderDecoder import FullEncode, FullDecode
import os

def clear():
    os.system("cls")

def save():
    global user_list
    f = open("EverydayLogin.txt","w")
    for user in user_list:
        for variable in user:
            f.write(f"{FullEncode(str(variable))};")
        f.write("\n")
    f.close()

def load():
    global user_list
    user_list = []
    try:
        f = open("EverydayLogin.txt","r")
        load_list = f.readlines()
        corrupt = False
        for user in load_list:
            splitUser = user.split(";")
            splitUser.pop(-1)
            if len(splitUser) != 6:
                corrupt = True
            pos = load_list.index(user)
            load_list[pos] = splitUser
        if not corrupt:
            for x in load_list:
                z: list = []
                for y in x:
                    z.append(FullDecode(y))
                user_list.append(z)
            return user_list
        else:
            print(f"CORRUPT SAVE FILE!")
            input(f"<")
            return "Corrupt"
    except OSError:
        print(f"NO LOADABLE SAVE FILE!")
        input(f"<")
        return "Corrupt"

def login():
    user_list = load()
    if user_list != "Corrupt":
        now: datetime = datetime.now()
        #print(f"Today's date is: {now:%d/%m/%y}")
        day_after = False
        Day: int = f'{now:%d}'
        Month: int = f'{now:%m}'
        Year: int = f'{now:%y}'
        current_user: str = input("Username: ")
        current_password: str = input("Password: ")
        correct_password: bool = False
        logged_user: list = []

        for user in user_list:
            if user[0] == current_user and user[1] == current_password:
                correct_password = True
                logged_user: list = user
        if correct_password:
            format = '%d/%m/%y'
            i = str(f"{logged_user[3]}/{logged_user[4]}/{logged_user[5]}")
            original = datetime.strptime(i, format).date()
            a = str(f"{Day}/{Month}/{Year}")
            current = datetime.strptime(a, format).date()
            difference = current - original
            duration =  difference.days
            if int(duration) == 1:
                print(f"Score: {logged_user[2]}.\nLast Login Date: {logged_user[3]}/{logged_user[4]}/{logged_user[5]}.\nCurrent Date: {now:%d/%m/%y}\n")
                logged_user[2] = int(logged_user[2])
                logged_user[2] += 1
                print(f"You've logged in {logged_user[2]} days in a row!\nLog in everyday to continue your streak!\n")
            elif int(duration) > 1:
                logged_user[2] = 1
                print(f"Score: {logged_user[2-1]}.\nLast Login Date: {logged_user[3]}/{logged_user[4]}/{logged_user[5]}.\nCurrent Date: {now:%d/%m/%y}\n")
                print(f"This could be the first of many!")
                print(f"It's been {int(duration)} days since you last logged in!\nLog in everyday to start a streak!\n")
            elif int(duration) < 1:
                print(f"Score: {logged_user[2]}.\nLast Login Date: {logged_user[3]}/{logged_user[4]}/{logged_user[5]}.\nCurrent Date: {now:%d/%m/%y}\n")
                print(f"You have already logged in today!\nLog in tommorrow to continue your streak!\n")
            if logged_user[3] != Day:
                logged_user[3] = Day
            if logged_user[4] != Month:
                logged_user[4] = Month
            if logged_user[5] != Year:
                logged_user[5] = Year
        else:
            print(f"Wrong username or password!")

def signup():
    valid_user = False
    while not valid_user:
        valid_user = True
        new_username: str = input("Username: ")
        new_password: str = input("Password: ")
        for user in user_list:
            if user[0] == new_username:
                print("Already a User with that Username!")
                valid_user = False
            if new_username == "":
                print("Username requires at least one character!")
                valid_user = False
        if " " in new_password:
            valid_user = False
            print("Password requires at least one character!")
        if ";" in new_password or "\\" in new_password:
            valid_user = False
            print("Password cannot contain the ';' or '\\\' or speech mark or non-QWERTY layout characters!")
    now: datetime = datetime.now()
    new_user = [new_username,new_password,'1',f'{now:%d}',f'{now:%m}',f'{now:%y}']
    user_list.append(new_user)

if __name__ == '__main__':
    while True:
        clear()
        log_or_sign: str = "yes"
        found = False
        while not found:
            log_or_sign: str = input("Login or Sign-Up? ")
            if log_or_sign == 'Login':
                user_login = True
                user_sign_up = False
                found = True
            elif log_or_sign == 'Sign-Up':
                user_login = False
                user_sign_up = True
                found = True
            else:
                input(f"{log_or_sign} is an invalid response. Please respond with 'Login' or 'Sign-Up'!")
        clear()
        while user_login:
            clear()
            login()
            if login() != "Corrupt":
                save()
            yn: str = input(f"Login as a different User (y/n)? ")
            yn.lower()
            if yn == 'n':
                user_login = False
        if user_sign_up:
            load()
            signup()
            save()
        clear()