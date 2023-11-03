import os
import random
import time

run = True
menu = True
play = False
fight = False
standing = True
fazFight = False

key = False
dragonFound = False
alive = True

HP = 80
MaxHP = HP
ATK = 10
Speed = 10
luck = 70
gold = 0
pot = 0
elix = 0
x = 0
y = 0
AC = 5
MOD = 0

map = [[" FOREST "," FOREST "," SWAMP  "," SWAMP  "],
       [" PLAINS "," FOREST "," SWAMP  ","MOUNTAIN"],
       ["  TOWN  ","  SHOP  ","  CAVE  ","MOUNTAIN"],
       [" DESERT ","  CAVE  "," HILLS  ","MOUNTAIN"],
       [" DESERT "," DESERT "," PLAINS "," HILLS  "]]

y_len = len(map)-1
x_len = len(map[0])-1

current_tile = map[y][x]

biome = {
    " PLAINS ": {
        "t": "PLAINS",
        "e": True},
    " DESERT ": {
        "t": "DESERT",
        "e": False},
    " SWAMP  ": {
        "t": "SWAMP",
        "e": True},
    "  TOWN  ": {
        "t": "TOWN",
        "e": False},
    "MOUNTAIN": {
        "t": "MOUNTAIN",
        "e": True},
    " HILLS  ": {
        "t": "HILLS",
        "e": True},
    " FOREST ": {
        "t": "FOREST",
        "e": True},
    "  CAVE  ": {
        "t": "CAVE",
        "e": True},
    "  SHOP  ": {
        "t": "SHOP",
        "e": False}
    }

e_list = ["RAT","2 RATS","3 RATS","18 RATS","GOBLIN","KIM-JONG-UN CULTIST","FREE SPEECH","SLIME"]

mobs = {
    "RAT": {
        "hp": 1,
        "at": 1,
        "go": 1,
        "ac": 2,
        "mo": 0
    },
    "2 RATS": {
        "hp": 2,
        "at": 2,
        "go": 2,
        "ac": 2,
        "mo": 0
    },
    "3 RATS": {
        "hp": 3,
        "at": 3,
        "go": 3,
        "ac": 2,
        "mo": 0
    },
    "18 RATS": {
        "hp": 18,
        "at": 18,
        "go": 18,
        "ac": 3,
        "mo": 1
    },
    "GOBLIN": {
        "hp": 30,
        "at": 6,
        "go": 40,
        "ac": 3,
        "mo": 0
    },
    "KIM-JONG-UN CULTIST": {
        "hp": 50,
        "at": 10,
        "go": 60,
        "ac": 4,
        "mo": 0
    },
    "FREE SPEECH": {
        "hp": 5,
        "at": 20,
        "go": 40,
        "ac": 4,
        "mo": 0
    },
    "SLIME": {
        "hp": 40,
        "at": 4,
        "go": 40,
        "ac": 3,
        "mo": 0
    },
    "KIM JONG UN": {
        "hp": 200,
        "at": 1,
        "go": 200,
        "ac": 5,
        "mo": -1
    },
    "FREDDY FAZBORE": {
        "hp": 999,
        "at": 999,
        "go": 99999,
        "ac": 15,
        "mo": 20
    },
    
}

def clear():
    os.system("cls")

def draw():
    print(f"┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")

def save():
    statsList = [
        name,
        str(HP),
        str(MaxHP),
        str(ATK),
        str(Speed),
        str(luck),
        str(gold),
        str(pot),
        str(elix),
        str(x),
        str(y),
        str(AC),
        str(MOD),
        str(dragonFound),
        str(alive),
        str(key)
    ]

    f = open("load.txt","w")
    for item in statsList:
        f.write(item + "\n")
    f.close()

def battle():
    global fight, play, run, HP, pot, elix, gold, Speed, AC, MOD, fazFight
    enemy = random.choice(e_list)
    if fazFight == True:
        enemy = "FREDDY FAZBORE"
        fazFight = False
    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["at"]
    g = mobs[enemy]["go"]
    ac = mobs[enemy]["ac"]
    mod = mobs[enemy]["mo"]

    draw()
    print(f"│YOU ARE BEING ATTACKED BY '{enemy}'")
    draw()
    input("│<━┛")
    while fight:
        clear()
        draw()
        print(f"│DEFEAT THE '{enemy}'!")
        draw()
        print(f"│{enemy}'S HP: {str(hp)}/{str(hpmax)}")
        print(f"│{enemy}'S AC: {ac}")
        print(f"│{enemy}'S ATK: {atk}")
        print(f"│{enemy}'S MODIFIER: {mod}")
        draw()
        print(f"│{name}'S HP: {HP}/{MaxHP}")
        print(f"│{name}'S AC: {AC}")
        print(f"│{name}'S ATK: {ATK}")
        print(f"│{name}'S MODIFIER: {MOD}")
        print(f"│{name}'S SPEED: {Speed}")
        print(f"│{name} HAS {pot} POTIONS AND {elix} ELIXIRS")
        draw()
        print(f"│1 - ATTACK")
        if pot > 0:
            print(f"│2 - USE POTION")
        if elix > 0:
            print(f"│3 - USE ELIXIR")
        print(f"│4 - RUN AWAY")
        draw()
        choice = input("│>")
        validChoice = False
        if choice == "1":
            validChoice = True
            rollToHit = random.randint(1,6)
            print(f"│YOU ROLLED A {rollToHit} +{MOD} = {rollToHit+MOD}.\n│{enemy}'S AC IS {ac}.")
            if rollToHit+MOD >= ac:
                print(f"│IT HITS! YOU DEAL {ATK} DAMAGE!")
                hp -= ATK
            else:
                print(f"│MISS.")
            draw()
        if choice == "2" and pot > 0:
            validChoice = True
            pot -= 1
            if HP < MaxHP:
                HP += 40
                if HP >= MaxHP:
                    HP = MaxHP
                    print(f"{name} DRANK A POTION, AND HEALED TO FULL HEALTH ({MaxHP})!")
                else:
                    print(f"{name} DRANK A POTION, AND HEALED 40 HP (to {HP})!")
        if choice == "3" and elix > 0:
            validChoice = True
            print(f"{name} DRANK AN ELIXIR, AND HEALED TO FULL HEALTH ({MaxHP})!")
            elix -= 1
            HP = MaxHP
        if choice == "4":
            validChoice = True
            escapeChance = random.randint(1,100)
            print(f"│YOU ROLLED {escapeChance}.\n│YOU NEEDED TO GET {100-Speed} OR HIGHER TO PASS.")
            if escapeChance >= 100-Speed:
                print(f"│YOU ESCAPE!")
                fight = False
            else:
                print(f"│YOU FAIL!")
                input("│<━┛")
        if validChoice == True and hp > 0 and fight == True:
            rollToHit = random.randint(1,6)
            print(f"│{enemy} ROLLED A {rollToHit} +{mod} = {rollToHit+mod}.\n│{name}'S AC IS {AC}.")
            if rollToHit+mod >= ac:
                print(f"│IT HITS! YOU TAKE {atk} DAMAGE!")
                HP -= atk
            else:
                print(f"│MISS.")
            draw()
            input("│<━┛")

        if HP <= 0:
            fight = False
            play = False
            run = False
            alive = False
            print(f"│{enemy} DEFEATED {name}!")
            print(f"│GAME OVER!")
            draw()
            input("│<━┛")
            save()
            quit()

        if hp <= 0:
            fight = False
            print(f"│{enemy} DEFEATED!")
            print(f"│YOU GET {g} GOLD!")
            gold += g
            draw()
            save()
            input("│<━┛")

        if validChoice == False:
            print(f"│INVALID COMMAND")
            standing = True
            input("│<━┛")

while run:
    while menu:
        clear()
        draw()
        print(f"│1. NEW GAME\n│2. LOAD GAME\n│3. CONTROLS\n│4. QUIT GAME")
        draw()
        choice = input("│>")
        validChoice = False
        if choice == "1":
            validChoice = True
            clear()
            name = input("│WHAT IS YOUR NAME? ")
            if name == "Dejan" or name == "DEJAN":
                for x in range(50):
                    print(f"│Dejan is a bad person.")
                time.sleep(1)
                clear()
                save()
                quit()
            menu = False
            play = True
            draw()
            print(f"│WELCOME {name}!")
            draw()
            input("│<━┛")

        if choice == "2":
            validChoice = True
            try:
                f = open("load.txt","r")
                load_list = f.readlines()
                if len(load_list) == 16:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    MaxHP = int(load_list[2][:-1])
                    ATK = int(load_list[3][:-1])
                    Speed = int(load_list[4][:-1])
                    luck = int(load_list[5][:-1])
                    gold = int(load_list[6][:-1])
                    pot = int(load_list[7][:-1])
                    elix = int(load_list[8][:-1])
                    x = int(load_list[9][:-1])
                    y = int(load_list[10][:-1])
                    AC = int(load_list[11][:-1])
                    MOD = int(load_list[12][:-1])
                    dragonFound = bool(load_list[13][:-1])
                    alive = bool(load_list[14][:-1])
                    key = bool(load_list[15][:-1])
                    clear()
                    draw()
                    print(f"│WELCOME BACK {name}!")
                    draw()
                    input("│<━┛")
                    menu = False
                    play = True
                else:
                    print(f"│CORRUPT SAVE FILE!")
                    input("│<━┛")
            except OSError:
                print(f"│NO LOADABLE SAVE FILE!")
                input("│<━┛")

        if choice == "3":
            validChoice = True
            clear()
            print(f"┣━━━━━━━━━━━━━━━━━━CONTROL━━━━━━━━━━━━━━━━━━━━┫\n│\n│TYPE THE NUMBER OF THE OPTION YOU WISH TO PICK\n│HP IS THE AMOUNT OF HEALTH YOU HAVE. DON'T DROP BELOW 0 OR YOU LOSE!\n│ATK IS THE DAMAGE YOU DEAL.\n│AC IS WHAT THE OPPONENT NEEDS TO ROLL TO HIT YOU.\n│MODIFIER IS WHAT YOU ADD TO YOUR ROLL TO HIT.\n│'>' MEANS YOU ARE EXPECTED TO INPUT A COMMAND.\n│'<━┛' MEANS PRESS 'ENTER' TO CONTINUE.\n│")
            input("│<━┛")

        if choice == "4":
            validChoice = True
            clear()
            quit()

        if validChoice == False:
            print(f"│THAT IS NOT A VALID CHOICE. ONLY TYPE THE NUMBER OF THE OPTION YOU WISH TO PICK.")
            input("│<━┛")

    while play:
        clear()
        save()
        if not alive or HP < 1:
            print(f"│{name} DIED. MAKE A NEW GAME.")
            input("│<━┛")
            
            name = "-CORPSE-"
            HP = 0
            MaxHP = "-CORPSE-"
            ATK = "-CORPSE-"
            Speed = "-CORPSE-"
            luck = "-CORPSE-"
            gold = "-CORPSE-"
            pot = "-CORPSE-"
            elix = "-CORPSE-"
            x = "-CORPSE-"
            y = "-CORPSE-"
            AC = "-CORPSE-"
            MOD = "-CORPSE-"
            dragonFound = "-CORPSE-"
            alive = False
            key = "-CORPSE-"
            save()
            quit()
        if not standing:
            if biome[map[y][x]]["e"]:
                if luck >= 100:
                    if random.randint(1,100) <= 1:
                        fight = True
                        battle()
                elif luck <= 0:
                    if random.randint(1,100) <= 99:
                        fight = True
                        battle()
                else:
                    if random.randint(1,100) >= luck:
                        fight = True
                        battle()
                        clear()
        draw()
        print(f"│LOCATION:",biome[map[y][x]]["t"])
        draw()
        for b in range(5):
            print(f"│",end="")
            for a in range(4):
                if a == x and b == y:
                    print(f"━    X     ",end="")
                else:
                    print(f"━ {map[b][a]} ",end="")
            print(f"━┫")

        draw()
        print(f"│NAME: {name}")
        if HP < MaxHP:
            if HP <= MaxHP-5:
                print(f"│HP: {HP}+5/{MaxHP}")
                HP += 5
            else: 
                dif = MaxHP-HP
                print(f"│HP: {HP}+{dif}/{MaxHP}")
                HP += dif
        else:
            print(f"│HP: {HP}/{MaxHP}")
        print(f"│ATK: {ATK}")
        print(f"│AC: {AC}")
        if MOD >= 0:
            print(f"│MODIFIER: +{MOD}")
        elif MOD < 0:
            print(f"│MODIFIER: {MOD}")
        print(f"│SPEED: {Speed}")
        print(f"│LUCK: {luck}")
        print(f"│POTIONS: {pot}")
        print(f"│ELIXIRS: {elix}")
        print(f"│GOLD: {gold}")
        print(f"│COORDS: ({x},{y})")
        draw()
        print(f"│0 ━ SAVE AND QUIT")
        n_option = False
        s_option = False
        e_option = False
        w_option = False
        locat = biome[map[y][x]]["t"]

        if y > 0:
            print(f"│1 ━ NORTH")
            n_option = True
        if y < y_len:
            print(f"│2 ━ SOUTH")
            s_option = True
        if x > 0:
            print(f"│3 ━ WEST")
            w_option = True
        if x < x_len:
            print(f"│4 ━ EAST")
            e_option = True
        if "SHOP" in locat:
            print(f"│5 ━ ENTER SHOP")
        draw()
        dest = input("│>")
        keyBind = False

        if dest == "0":
            keyBind = True
            save()
            play = False
            menu = True
        if dest == "1" and n_option == True:
            keyBind = True
            if y > 0:
                y -= 1
                standing = False
        if dest == "2" and s_option == True:
            keyBind = True
            if y < y_len:
                y += 1
                standing = False
        if dest == "3" and w_option == True:
            keyBind = True
            if x > 0:
                x -= 1
                standing = False
        if dest == "4" and e_option == True:
            keyBind = True
            if x < x_len:
                x += 1
                standing = False
        if dest == "DRAGON!" and "MOUNTAIN" in locat:
            keyBind = True
            clear()
            print("┣━━━━━━━━━━━━━━━━DRAGON LAIR━━━━━━━━━━━━━━━━━━┫")
            if dragonFound == True:
                print("│HOW DARE YOU RETURN!\n│I SHOULD SMITE YOU WHERE I STAND!\n│BECAUSE I'M FEELING GENEROUS, I'LL LET YOU GO...\n│ON ONE CONDITION!\n│YOU SLAY MY CHAMPION!!!")
                input("│<━┛")
                print("@#@@@@@@@@@@@@@@@@@@@@@@@#+@;##+'++####@@@@@@@@+#'+'+##+'+';;;+@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                print("++####@@@@@@@@@@@@@@@@@@#+@+@##++#+###@#@@@##@@@@#####@+@#+''+@#@@@@@@@@@@@@@@@@@@@@@@####")
                print("++#+++###@@@@@@@@@@@@@@@@@@@@@##@###@@@#@@@@@@@###@##@#@@+@#@@@+@@@@@@@@@@@@@@@@@@###+####")
                print("+++#'++++#@@@@@@@@@@@@@@#####@@@@@@@@@@@#@@#@#####################@@@@@@@@@@@@@@@##+#++#++")
                print("+###++++++#@@@@@@@@@@@@#+#####++++++#+#+##+####+####################@@@@@@@@@@@@####+++###")
                print("++##+++++++#@@@@@@@@@###+####+++++#++++++++#+++#++###################@@@@@@@@@@@###+######")
                print("######+++++#@@@@@@@@###+####+#+++++++++++++++'+++++##############@####@@@@@@@@@###+####@##")
                print("@@@@@@@@++++##@@@@@##++####+++++++'+++++''+++++#++######+##############@@@@@@@#++###@@@@@@")
                print("#@#@###@@#+++#@@@@###++##++'##++'++'+++++'++'''++#+#####++##############@@@@@@#+##@@@####@")
                print("#########@#+++@@@@@##++###++#+##++'''+##'+++'+'+++#+#+##+++#++###########@@@@#++#@@#######")
                print("##########@+++@@@@###+++++++++++++'+++##++++'''''+++++++++++++++#########@@@@++#@@########")
                print("###########@+#@@@####''++'''++##+++++#+#+++'''''+''+++++++++++++##########@@@#+#@#########")
                print("###+#++####@++@@@###+''++'+'+++#++++###++++++''+''+++++++++'+'+++#+##+####@@@#+@@#########")
                print("#++++++#####+#@@###+'##+++++++#++++++#+++++++'+'+''''+'+++++''+++++#+######@@##@@#########")
                print("++++++++###++#@@####'++###++++++++++++++'+++++''''''++++++'+++++++++++#####@@@+#@#########")
                print("#+++++++##@++@#@+#+#++++##+'''+'++++++++++++++'+++''++++++'++++++++++#++###@@@#+@#########")
                print("#+++++++###++@@###+#+'++##++''+++++++++++++++++++''''++++++++++++++++++#####@@#+@@########")
                print("##++++++#@'+@@@++++''++#+++++++++#++++++++++++++++++''+++++++++++++++'+#####@@@++@########")
                print("++++++++##+#@;@+#++;''++++++++++###++++++++++++++++#++'+'++++++#+++++'+++###;#@#+@@#######")
                print("#+#+++###++#@@#++++'''+++#++++++####+##++++++'++++++'++++'+++++++++++++#####@@@@+#@#######")
                print("####++##@++@@@##+++'';'+++@@@@@@@@@#+++#+++#+++++'++++++#@@@@@@@@#+++++++####@@@#+@@######")
                print("###+####++#@@@+++++;;'''@@@@@@@@@@@@@@@#+##+#####+++#@@@@@@@@@@@@@@@+++++####@@@#+#@######")
                print("#######@'#@@@##+++'''''+@@@@@@@@@@@@@@@@@+++++#+++#@@@@@@@@@@@@@@@@@+''+++###@@@@++@@#####")
                print("#@@@@@##+#@@@#+#++';'';'@@@@@@@@@@@@@@@@#+++++++++#@@@@@@@@@@@@@@@@@'+++++++##@@@#+#@@@@#@")
                print("######+++@@@@++++#'''''+@@@@@@@@@@@@@@@#+'+++++++++#@@@@@@@@@@@@@@@++++'+++++#@@@@#++#####")
                print("#++#++++#@@@#++++''''+'+@@@@@##+'+'+++++'++++++++++++++####+##@@@@@+++++++'+###@@@@#++####")
                print("+++##++#@@@##++++;''+''+#@@#+++++++++++++++++#++++++++##+++++++#@@@+++++'++++###@@@####+++")
                print("##+##@@@@@@###++'''''''++++++++++##+'+++++++##+++++++++####++++++++++++++'''+###@@@@@@####")
                print("@@@@@@@@@@@####+'''''+++++++#@@@@@@@#++'+'++++++++++++@@@@@@@##+++++'+++++++++##@@@@@@@@@@")
                print("@@@@@@@@@@@####''''''''++###@@@@#@@@@@@'++++++++++++#@@#@@@@@@@#++''+++++++'++##@@@@@@@@@@")
                print("@@@@@@@@@@@####''';'''+'+##@@@@@@@@@@@@#+++++++++++#@@@@@@@@@@#@#+'++'++++++++##@@@@@@@@@@")
                print("@@@@@@@@@@####'''';;''+++##@@@@@@@@@@@@@++++++++++#@@@@@@@@###@@@#+++++#++++++##@@@@@@@@@@")
                print("@@@@@@@@@@###+';;'''''''+@@@@@@@;:,@@@@@#+++#+++++#@@:     :@@@#@@+++++++++#+++#@@@@@@@@@@")
                print("@@@@@@@@@@###';;';++''++#@@#:.`.:,:'@@@@@+++++++++;,``,:,:   `@@@@++++#+++++'#+#@@@@@@@@@@")
                print("@@@@@@@@@@##+';''''+++++#@@':.; ...,@@@@@###+++++#:,`; ...`   @@@@#++++#++++++##@@@@@@@@@@")
                print("@@@@@@@@@@+#''''''+'++++@@@':.;:@@@,@@@@@##++++++#:,``'@@.    @@@@@+++##+++++####@@@@@@@@@")
                print("@@@@@@@@@#+++''+'''+++++@@@#:,''@@@,@@@@@++#++#++#;,,'#@@;:   @@@@@#++#++++++####@@@@@@@@@")
                print("@@@@@@@@@++'++'''';'''++@@@@:,++@@':+@@@@##+++##+#;,.++@@;;   @@@@@#+++++++++#####@@@@@@@@")
                print("@@@@@@@#+++'+'+''''''''+#@@@;,.@@#+++@@@@##+++##+#::,'@##'    @@#@@#'+#+++++#+#+###@@@@@@@")
                print("@@@@@@#+#+'';';'''';'''+#@@@+:,``,  @@@@@@@@@@@@@@@+,.`';     @@@@@#++++++++#+#+####@@@@@@")
                print("@@@@@@+++''';';;';;;''+'+@@@@;:.`` `@@@@@@@@@@@@@@@@@@@`     @@@@@#++'#+#+##++++#####@@@@@")
                print("@@@@@#+'+'';'';;'';;'''++#@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@`  :@@@@@#++++++++++'+##+####@@@@@")
                print("@@@@@+''+'''';;::;;;';''+++@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##++''+++++++++#+#####@@@@")
                print("@@@@#+'''+'+';;;;;;;;''+++#@@@#@@@@@#@@@@@@@@@@@@@@@@@@@@#@@@@@####+++++#+++++++++####@@@@")
                print("@@@@#+''++'+'';';;'''++###+++##+##@@.@@@@@@@@@@@@@@@@@@'@@@#########++#++##++++++++###@@@@")
                print("@@@@#+'''''++''';;''++##+++++++++##@@@@@@@@@@@@@@@@@@@@@@###+###########+#++++++#++####@@@")
                print("@@@@#+'''''+'';';';'##+''++'+++++++#@+#@@@@@@@@@+'::+@@@####++#++###+####+#++#++##++###@@@")
                print("@@@@#+''+'''';;';;#++';''++'+'+'++++#@@@@@@@@@@@#@@@@@@##++#+++'+'+++++##++#+++++#++###@@@")
                print("@@@@##+'''';;;;;;#'';';''++'+'''''''''+@@@@@@@@@@@@@@###+++++++++++#+'++###++++##++++##@@@")
                print("@@@@#+'''''';;'';+'';'';''''''''+''''';+++#@@@@@@#++#++#+++++++++++++++++#++++++#+++##@@@@")
                print("@@@@##'''''';;;;#';;;;';''';'''''+';;''+'++++++++++++++++++++'+++++''+''++#++#+++#++##@@@@")
                print("@@@@@#+++';''';'';;;;@#;'''';'';;';';;;''''''+#''''++++'+++++'+'+''''@''++++++++##+###@@@@")
                print("@@@@@#'+++''';''';:;:@#;''@@';;;';;'';;;''''''#''''''''+''''++++@@'''@+'''+#++++##+###@@@@")
                print("@@@@@##+++;:';'+';::;;;;;;;'';;';'';'''';'''''+'''''+''''';'+'++''''''''++'+++++#++##@@@@@")
                print("@@@@@@##+;;;;'+';::;::::;;:';;''''''';''';'''''';'''''''''''''''''''''''#'''+#+##+###@@@@@")
                print("@@@@@@##+'''''''::::;;':;::;''''''''''''''''''''''+''''';'''''''''''+'''''''###+####@@@@@@")
                print("@@@@@@@##++'+'+':;';;:@@:;:;'''''''''''''''''''''''''''';;''''''''''@@'''''+#######@@@@@@@")
                print("@@@@@@@@##+++++';';;;;''':;;;''''''''''';;''''''''''''''''''''''''''''''''''######@@@@@@@@")
                print("@@@@@@@@@+#++##+'':';;;;;;';';''''+''''''''''''''+'''''''''''''''''''''''''+#####@@@@@@@@@")
                print("@@@@@@@@@@#+#+##+';'''';';;';'''''''''''''''''''''''''''''''''''''+'+''''+'####@@@@@@@@@@@")
                print("@@@@@@@@@@@#####+'''''+';';'''''''''''''''''+''+''+'''''''''''''+'+++++'''++###@@@@@@@@@@@")
                print("@@@@@@@@@@@@####+++++'';'++'+'''++'+'''''''''+''++++'+'''''''+++++++++'''+###@@@@@@@@@@@@@")
                print("@@@@@@@@@@@@@@+##++''+'''+++++'++++++++'''''++'+++'+'''''''++++++++'++++++#@#@@@@@@@@@@@@@")
                print("@@@@@@@@@@@@@@+'#++++'+++''+'++++++++++++'''++''++++''+++'''++++++++++#++####@@@@@@@@@@@@@")
                print("@@@@@@@@@@@@@@++#@++++++'++++++++++++++++++'+++++++++++'++++++++++++#+##+####@@@@@@@@@@@@@")
                print("@@@@@@@@@@@@@@+++@@#++++++++++++++++++++++++++++++'++++++++++++#++#####@#####@@@@@@@@@@@@@")
                print("@@@@@@@@@@@@@@+'#@@@###+###+++++#+#++++++++++++++++++++++++++###+######@#####@@@@@@@@@@@@@")
                print("@@@@@@@@@@@@@@+'+#@@@@##@########++++++++++++++++++++++############@#@@#@##++@@@@@@@@@@@@@")
                print("@@@@@@@@@@@@@@++##@@@@@@@@+#@@@@###############+#+########@@##@+'###@##@##+#+@@@@@@@@@@@@@")
                print("@@@@@@@@@@@@@@+++##@@@@@@@'#@@@@@@@@@@@@@@@@@@@@@@@@@@@#:`@@@#@#'@@@@@@@##++#@@@@@@@@@@@@@")
                print("@@@@@@@@@@@@@@+#+###@@@@@@'#@++'+'+'@@@@@@@@@@@@#+'';##'+#''''@''+@@@@@#####+@@@@@@@@@@@@@")
                print("@@@@@@@@@@@@@@++#+####@@@@:@@,:;;;;;##+'''#''';:'''''+@';;;;;:@;;+@@@@########@@@@@@@@@@@@")
                print("@@@@@@@@@@@@@@##++++++##@@;@@.:::::,;':;;;;;@@'@;::;;;:;,::::,@:,'@@##########@@@@@@@@@@@@")
                print("@@@@@@@@@@@@@@+#++'''+######@.:::,,,@+::::,,@@@@::,:,:@#,,,,,.@@@######++#####@@@@@@@@@@@@")
                print("@@@@@@@@@@@@@@+'+''++'''+########;.`@',,,.,.@@@@;,,,..@@,:'@@@##########++++#@@@@@@@@@@@@@")
                print("@@@@@@@##@@@@@++'+++;'''++++###########@@#@#####@#@@@##@########+#+++++++##+#@@@@@@@@@@@@@")
                print("@@@#########@@#++'++'';'++++++###############+#@##@#@##+##++#+++++++'+++++#+###########@@@")
                print("@#+##########@+++''+''++'++++'++++++###+###++########+++##+++++++++++++##+#+##############")
                print("###++######@@@#++''++''''+#'+#+++###+'+++#++++#++++++++#++'++++++++++++##+################")
                print("+++#####+##@@@@#+''++'''+'+#+++#++++++++++++++#++++++++++#++'++++++++###+#################")
                print("+++#########@@@#+'++++++''+'#++++'++++++'+++++#++++++++'+++++++#+++#+#######@#############")
                print("+#++####@#@#@@@@#++'+++''+'+'+'++'++++++'+++++++''+++++++++++++###+##+#####@@########+####")
                print("+++++#+####@@@@@@#++#+++#++++++++''+++++++++++++'''+++++++++++###++########@@########++##+")
                print(";#++#+#####@@@@@@@##+++++++++++++++++++++++##+++'+'+++++++++##+###########@@@@#########++#")
                print("++'+++#####@@@@@@@@#+##+#+++#++#+++++++++#+##+++++++++++++#+#############@@@@@#######+++++")
                print("'''++#++##@@@@@@@@@@###+#+###+##+++++++++++###++++++#++++################@@@@@######++++''")
                print(";''+++++###@@@@@@@@@#############+###+++#+###++++##+++++#################@@@@@#####++++++'")
                print(";''++++#####@@@@@@@###.############++++#######+++++#+#####################@+@@@#+#++'+++'+")
                print("+;''+'+####@@@@@@@####+@+###########+##########+++############@@###@###+##@@@@@###++++++''")
                print("@#'''+++###@@@@@@+###++.#@@###########++################@#@##@@@@@'@######@@@@@#++#++++'+@")
                input("│<━┛")
                fazFight = True
                fight = True
                battle()
                print("│BECAUSE YOU SUCCEEDED IN KILLING MY CHAMPION, I WILL SPARE YOU!\n│LEAVE, BEFORE I CHANGE MY MIND!")
                input("│<━┛")
            if dragonFound == False:
                print("│YOU HAVE FOUND MY LAIR!\n│AS A REWARD, YOU MAY SET YOUR GOLD TO WHATEVER VALUE!\n│HOW MUCH DO YOU WISH TO OWN?")
                gold = int(input("│>"))
                print("│YOU ARE WELCOME MORTAL, NOW DO NOT RETURN!")
                input("│<━┛")
                dragonFound = True
        if dest == "5" and "SHOP" in locat:
            clear()
            keyBind = True
            print(f"┣━━━━━━━━━━━━━━━━━━━━SHOP━━━━━━━━━━━━━━━━━━━━━┫\n│\n│TYPE THE NUMBER OF THE ITEM YOU WISH TO BUY\n│")
            draw()
            if name == "Knoryh | ||":
                print(f"│0 ━ 0 GOLD ━ GOD MODE.")
            if gold >= 5:
                print(f"│1 ━ 5 GOLD ━ INVERT LUCK.")
            if gold >= 10:
                print(f"│2 ━ 10 GOLD ━ EXCHANGE BETWEEN STATS.")
            if gold >= 15:
                print(f"│3 ━ 15 GOLD ━ BUY A POTION.")
            if gold >= 40:
                print(f"│4 ━ 40 GOLD ━ BUY A ELIXIR.")
            if gold >= 50:
                print(f"│5 ━ 50 GOLD ━ +5 TO HP, SPEED AND LUCK.")
                print(f"│6 ━ 50 GOLD ━ +15 TO HP, SPEED OR LUCK.")
                print(f"│7 ━ 50 GOLD ━ +5 TO ATK.")
                print(f"│8 ━ 50 GOLD ━ +1 TO AC OR MODIFIER.")
            if gold >= 100:
                print(f"│9 ━ 50 GOLD ━ TELEPORTER.")
                print(f"│10 ━ 100 GOLD ━ WOODEN SWORD.")
            if gold >= 150:
                print(f"│11 ━ 150 GOLD ━ STONE SWORD.")
            if gold >= 200:
                print(f"│12 ━ 200 GOLD ━ BRONZE SWORD.")
            if gold >= 300:
                print(f"│13 ━ 300 GOLD ━ SILVER SWORD.")
            if gold >= 400:
                print(f"│14 ━ 400 GOLD ━ GOLD SWORD.")
            if gold >= 500:
                print(f"│15 ━ 500 GOLD ━ OBSIDIAN SWORD.")
            if gold >= 1000:
                print(f"│16 ━ 1000 GOLD ━ GODS BLADE.")
            draw()
            shopItem = input("│>")
            validInput = False
            if shopItem == "0" and name == "Knoryh | ||":
                validInput = True
                clear()
                print(f"┣━━━━━━━━━━━━━━━━━━━━SHOP━━━━━━━━━━━━━━━━━━━━━┫\n│\n│TYPE THE ITEMS COST TO BUY\n│")
                draw()
                print(f"│0 GOLD ━ GOD MODE.")
                spent = input("│>")
                if spent == "0":
                    print("│MAX HP")
                    MaxHP = int(input("│>"))
                    print("│ATK")
                    ATK = int(input("│>"))
                    print("│SPEED")
                    Speed = int(input("│>"))
                    print("│LUCK")
                    luck = int(input("│>"))
                    print("│AC")
                    AC = int(input("│>"))
                    print("│MODIFIER")
                    MOD = int(input("│>"))

            if shopItem == "1" and gold >= 5:
                validInput = True
                clear()
                print(f"┣━━━━━━━━━━━━━━━━━━━━SHOP━━━━━━━━━━━━━━━━━━━━━┫\n│\n│TYPE THE ITEMS COST TO BUY\n│")
                draw()
                print(f"│5 GOLD ━ INVERT LUCK.")
                print(f"│YOUR LUCK ({luck}) WILL BE REVERSED ({100-luck}).\nGOOD IF YOU WISH TO CHANGE YOUR MONSTER SPAWN CHANCE.")
                draw()
                spent = input("│>")
                if spent == "5":
                    luck = 100-luck
                    gold -= 5
            if shopItem == "2" and gold >= 10:
                validInput = True
                clear()
                print(f"┣━━━━━━━━━━━━━━━━━━━━SHOP━━━━━━━━━━━━━━━━━━━━━┫\n│\n│TYPE THE ITEMS COST TO BUY\n│")
                draw()
                print(f"│10 GOLD ━ EXCHANGE BETWEEN STATS.")
                print(f"│-15 TO HP, SPEED, -5 TO ATK, -1 to AC OR MODIFIER")
                print(f"│+15 TO HP, SPEED, LUCK, +5 TO ATK, +1 to AC OR MODIFIER")
                draw()
                spent = input("│>")
                if spent == "10":
                    lowerDone = False
                    while not lowerDone:
                        print(f"│WHICH STAT DO YOU WISH TO LOWER?")
                        lowerStat = input("│>")
                        if lowerStat == "HP":
                            MaxHP -= 15
                            lowerDone = True
                        if lowerStat == "SPEED":
                            Speed -= 15
                            lowerDone = True
                        if lowerStat == "ATK":
                            ATK -= 5
                            lowerDone = True
                        if lowerStat == "AC":
                            AC -= 1
                            lowerDone = True
                        if lowerStat == "MODIFIER":
                            MOD -= 1
                            lowerDone = True
                    higherDone = False
                    while not higherDone:
                        print(f"│WHICH STAT DO YOU WISH TO BUFF?")
                        lowerStat = input("│>")
                        if lowerStat == "HP":
                            MaxHP += 15
                            higherDone = True
                        if lowerStat == "SPEED":
                            Speed += 15
                            higherDone = True
                        if lowerStat == "LUCK":
                            luck += 15
                            higherDone = True
                        if lowerStat == "ATK":
                            ATK += 5
                            higherDone = True
                        if lowerStat == "AC":
                            AC += 1
                            higherDone = True
                        if lowerStat == "MODIFIER":
                            MOD += 1
                            higherDone = True
                    gold -= 10
            if shopItem == "3" and gold >= 15:
                validInput = True
                clear()
                print(f"┣━━━━━━━━━━━━━━━━━━━━SHOP━━━━━━━━━━━━━━━━━━━━━┫\n│\n│TYPE THE ITEMS COST TO BUY\n│")
                draw()
                print(f"│15 GOLD ━ BUY A POTION.")
                print(f"│HEALS YOU BY 40!")
                draw()
                spent = input("│>")
                if spent == "15":
                    pot += 1
                    gold -= 15
            if shopItem == "4" and gold >= 40:
                validInput = True
                clear()
                print(f"┣━━━━━━━━━━━━━━━━━━━━SHOP━━━━━━━━━━━━━━━━━━━━━┫\n│\n│TYPE THE ITEMS COST TO BUY\n│")
                draw()
                print(f"│40 GOLD ━ BUY AN ELIXIR.")
                print(f"│HEALS YOU BACK YOU MAX!")
                draw()
                spent = input("│>")
                if spent == "40":
                    elix += 1
                    gold -= 40
            if shopItem == "5" and gold >= 50:
                validInput = True
                clear()
                print(f"┣━━━━━━━━━━━━━━━━━━━━SHOP━━━━━━━━━━━━━━━━━━━━━┫\n│\n│TYPE THE ITEMS COST TO BUY\n│")
                draw()
                print(f"│50 GOLD ━ +5 TO HP, SPEED AND LUCK.")
                draw()
                spent = input("│>")
                if spent == "50":
                    MaxHP += 5
                    Speed += 5
                    luck += 5
                    gold -= 50
            if shopItem == "6" and gold >= 50:
                validInput = True
                clear()
                print(f"┣━━━━━━━━━━━━━━━━━━━━SHOP━━━━━━━━━━━━━━━━━━━━━┫\n│\n│TYPE THE ITEMS COST TO BUY\n│")
                draw()
                print(f"│50 GOLD ━ +2 TO AC AND MODIFIER.")
                draw()
                spent = input("│>")
                if spent == "50":
                    AC += 2
                    MOD += 2
                    gold -= 50
            if shopItem == "7" and gold >= 1000:
                validInput = True
                clear()
                print(f"┣━━━━━━━━━━━━━━━━━━━━SHOP━━━━━━━━━━━━━━━━━━━━━┫\n│\n│TYPE THE ITEMS COST TO BUY\n│")
                draw()
                print(f"│1000 GOLD ━ GODS BLADE.")
                print(f"│BECOME A PALADIN OF THE LORD!")
                spent = input("│>")
                if spent == "1000":
                    MaxHP += 50
                    Speed += 50
                    ATK += 10
                    AC += 5
                    MOD += 5

                    gold -= 1000
                
            if validInput == False:
                print(f"│INVALID COMMAND")
        
        if keyBind == False:
            print(f"│INVALID COMMAND")
            standing = True
            input("│<━┛")