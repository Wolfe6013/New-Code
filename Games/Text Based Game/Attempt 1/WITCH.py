import random, os, time, sys

if not True:
            #clear()
            #draw(False)
            print("THE \033[1;30;40mWITCH\033[0m APPEARS!")
            #draw(False)
            print("│<")
            #time.sleep(1)

while True:
    while True:
        while True:
            os.system("cls")
            Gray = "\033[1;30;40m"
            Red = "\033[1;31;40m"
            Green = "\033[1;32;40m"
            Yellow = "\033[1;33;40m"
            Blue = "\033[1;34;40m"
            Purple = "\033[1;35;40m"
            Cyan = "\033[1;36;40m"
            End = "\033[0m"

            colList = [Red,Green,Yellow,Blue,Purple,Cyan]

            text1 = "THE "
            text2 = "WITCH"
            text3 = " APPEARS!"

            for char in text1:
                print(char,end="")
                sys.stdout.flush()
                time.sleep(0.05)
            print(Gray,end="")
            for char in text2:
                print(char,end="")
                sys.stdout.flush()
                time.sleep(0.05)
            print(End,end="")
            for char in text3:
                print(char,end="")
                sys.stdout.flush()
                time.sleep(0.05)

            time.sleep(1)
            os.system("cls")

            colList = [Red,Green,Yellow,Blue,Purple,Cyan]
            Rand1 = random.choice(colList)
            print(f"THE {Gray}WIT{Rand1}C{Gray}H{End} APPEARS!")
            time.sleep(0.9)
            os.system("cls")
            
            colList = [Red,Green,Yellow,Blue,Purple,Cyan]
            Rand1 = random.choice(colList)
            print(f"THE {Gray}W{Rand1}I{Gray}TCH{End} APPEARS!")
            time.sleep(0.8)
            os.system("cls")
            
            colList = [Red,Green,Yellow,Blue,Purple,Cyan]
            Rand1 = random.choice(colList)
            print(f"THE {Gray}WITC{Rand1}H{End} APPEARS!")
            time.sleep(0.7)
            os.system("cls")
            
            colList = [Red,Green,Yellow,Blue,Purple,Cyan]
            Rand1 = random.choice(colList)
            colList.remove(Rand1)
            Rand2 = random.choice(colList)
            print(f"THE {Rand1}W{Rand2}I{Gray}TCH{End} APPEARS!")
            time.sleep(0.6)
            os.system("cls")
            
            colList = [Red,Green,Yellow,Blue,Purple,Cyan]
            Rand1 = random.choice(colList)
            colList.remove(Rand1)
            Rand2 = random.choice(colList)
            print(f"THE {Gray}WI{Rand1}T{Gray}C{Rand2}H{End} APPEARS!")
            time.sleep(0.5)
            os.system("cls")
            
            colList = [Red,Green,Yellow,Blue,Purple,Cyan]
            Rand1 = random.choice(colList)
            colList.remove(Rand1)
            Rand2 = random.choice(colList)
            print(f"THE {Gray}W{Rand1}I{Gray}T{Gray}C{Rand2}H{End} APPEARS!")
            time.sleep(0.4)
            os.system("cls")
            
            colList = [Red,Green,Yellow,Blue,Purple,Cyan]
            Rand1 = random.choice(colList)
            colList.remove(Rand1)
            Rand2 = random.choice(colList)
            colList.remove(Rand2)
            Rand3 = random.choice(colList)
            print(f"THE {Gray}W{Rand1}I{Rand2}T{Gray}C{Rand3}H{End} APPEARS!")
            time.sleep(0.3)
            os.system("cls")
            
            colList = [Red,Green,Yellow,Blue,Purple,Cyan]
            Rand1 = random.choice(colList)
            colList.remove(Rand1)
            Rand2 = random.choice(colList)
            colList.remove(Rand2)
            Rand3 = random.choice(colList)
            print(f"THE {Rand1}W{Gray}I{Rand2}T{Gray}C{Rand3}H{End} APPEARS!")
            time.sleep(0.2)
            os.system("cls")
            
            colList = [Red,Green,Yellow,Blue,Purple,Cyan]
            Rand1 = random.choice(colList)
            colList.remove(Rand1)
            Rand2 = random.choice(colList)
            colList.remove(Rand2)
            Rand3 = random.choice(colList)
            colList.remove(Rand3)
            Rand4 = random.choice(colList)
            print(f"THE {Rand1}W{Rand2}I{Rand3}T{Gray}C{Rand4}H{End} APPEARS!")
            time.sleep(0.1)
            os.system("cls")
            for x, y in enumerate(range(100)):        
                colList = [Red,Green,Yellow,Blue,Purple,Cyan]
                Rand1 = random.choice(colList)
                colList.remove(Rand1)
                Rand2 = random.choice(colList)
                colList.remove(Rand2)
                Rand3 = random.choice(colList)
                colList.remove(Rand3)
                Rand4 = random.choice(colList)
                colList.remove(Rand4)
                Rand5 = random.choice(colList)
                print(f"THE {Rand1}W{Rand2}I{Rand3}T{Rand4}C{Rand5}H{End} APPEARS!")
                os.system("cls")

            print(f"THE {Gray}WITCH{End} APPEARS!")
            time.sleep(1)
            os.system("cls")
            input()