from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    page = 0
    if '<@1210937429880602714>' in lowered or '<@&1210939671291498528>' in lowered:
        if 'open' in lowered:
            try:
                f = open("Book.txt","r")
                load_list = f.readlines()
                return (load_list[page][:-1])
            except OSError:
                print(f"NO LOADABLE SAVE FILE!")
        elif '>' in lowered:
            try:
                page += 1
                f = open("Book.txt","r")
                load_list = f.readlines()
                return (load_list[page][:-1])
            except OSError:
                print(f"NO LOADABLE SAVE FILE!")
        elif '<' in lowered:
            try:
                page -= 1
                f = open("Book.txt","r")
                load_list = f.readlines()
                return (load_list[page][:-1])
            except OSError:
                print(f"NO LOADABLE SAVE FILE!")
        elif 'help' in lowered:
            return f"To use a command, simply <@1210579164944404520> (either the bot or the role) and write the command following that.\nTo get the bot to message you privately, start your message with a '?'\ngamble - offers to the Shrine of Chance. Wonder what you'll get!\nroll d4 - rolls a four sided dice and gives you the outcome.\nroll d6 - rolls a six sided dice and gives you the outcome.\nroll d8 - rolls an eight sided dice and gives you the outcome.\nroll d10 - rolls a ten sided dice and gives you the outcome.\nroll d12 - rolls a twelve sided dice and gives you the outcome.\nroll d20 - rolls a twenty sided dice and gives you the outcome.\nflip coin - flips a coin and gives you the outcome.\nhelp - tells you every command available"
        else:
            return "Unknown command, try 'help' for more info"