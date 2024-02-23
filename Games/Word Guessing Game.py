import random, sys, os

def clear():
    os.system("cls")

play = True

while play:
    yn = input("Do you want to play a game? (y/n) ")
    if yn == "y":
        words = "zippy","pointless","post","tremble","coherent","spiky","icky","letters","van","trite","four","behavior","spurious","plot","caption","time","conscious",'snobbish','earthquake','maddening','alleged','first','faint','ordinary','rigid','compete','tin','political','driving','thunder','battle','flowery','gaping','luxuriant','floor','scent','impress','wing','dare','position','hand','abhorrent','poison','woozy','halting','puzzling','possess','vase','locket','volcano','pick','kiss','accessible','heartbreaking','risk','reason','seal','vagabond','wide','visit','observant','flight','multiply','relax','wander','sophisticated','crazy','contain','passenger','ashamed','fill','unruly','wanting','step','zipper','argue','descriptive','overjoyed','beam','disarm','song','tug','ceaseless','daily','two','obeisant','precious','frightening','jellyfish','puny','distance','pies','earn','smiling','early','unequal','calendar','pray','chop','shaggy','knit','snails','soup','door','trouble','live','club','line','actor','late','general','lick','cub','knee','spooky','play','harbor','wonderful','analyze','store','unsightly','bells','pleasant','ambitious','fool','protect','unaccountable','fence','oceanic','second','abstracted','wound','low','tour','painful','dynamic','reaction','pink','phone','medical','swim','history','gruesome','rabbit','invincible','brush','acceptable','round','pest','protest','twig','committee','entertain','mourn','cultured','efficient','oil','grate','silly','group','bored','annoy','racial','godly','left','respect','grumpy','hall','object','nest','shelf','float','laughable','act','creator','anger','scissors','insect','extend','tangible','measly','telling','mind','market','quill','alike','permissible','texture','shrug','grab','bounce','growth','ugly','infamous','sip','tedious','wooden','juicy','cheerful','actually','trap','deserve','amused','excuse','irate','crush','underwear','zip','window','bike','queen','pollution','oatmeal','volleyball','pop','son','land','scrub','irritating','bag','handsomely','tired','party','profit','structure','productive','flat','burn','habitual','verdant','visitor','domineering','quicksand','aquatic','warn','fang','wail','squeeze','kneel','questionable','quizzical','animated','parallel','freezing','plug','quirky','ear','earthy','cattle','collect','front','sweet','jail','chance','earth','snotty','vest','pie','return','belong','theory','brainy','merciful','lame','truculent','street','hallowed','title','spell','hum','ancient','tender','dog','stormy','panicky','baseball','suit','warlike','mark','cactus','exuberant','quaint','limping','chunky','price','lazy','nail','overflow','elderly','dizzy','agonizing','delightful','best','awful','cellar','closed','three','poised','eyes','wakeful','check','cause','clap','aboard','ship','bumpy','admire','rude','cluttered','messy','fasten','button','tray','old','blink','appreciate','elastic','chief','small','male','celery','men','languid','look','vengeful','shade','horses','steam','crowded','stupendous','influence','educated','grouchy','shelter','penitent','victorious','books','borrow','telephone','health','aloof','motionless','wax','brother','great','thrill','dirt','pot','tight','divide','cars','groan','private','pumped','reflective','romantic','vanish','run','umbrella','paint','refuse','cent','keen','cup','deadpan','flavor','meeting','amazing','ritzy','brake','seemly','table','question','show','wool','woman','metal','blind','gaze','jumbled','travel','drain','sweater','prevent','twist','good','greedy','planes','fact','quiet','lethal','hissing','grey','activity','unsuitable','development','elite','noiseless','beautiful','hat','rest','aboriginal','receive','nippy','selfish','pocket','daughter','assorted','ducks','hate','scorch','energetic','puzzled','jeans','vast','signal','snore','rhythm','youthful','cart','macabre','slippery','combative','frogs','stir','fine','scarf','sign','yard','secretary','inject','picture','salty','lean','furniture','arrive','spoon','tickle','voice','imaginary','pour','base','meal','farm','sparkle','develop','true','fretful','bit','silky','wrathful','angry','hanging','swanky','nondescript','whip','pencil','lewd','foregoing','power','milky','sneeze','decorate','windy','snow','haunt','steer','spiders','squeak','female','hateful','duck','lively','dislike','search','coach','tasteful','gray','mundane','insidious','carve','phobic','nutty','prick','tree','person','festive','flawless','prickly','slimy','decide','drop','snatch','concern','disagreeable'

        correctWord = random.choice(words)
        guess = []
        guess = list(guess)
        wrongGuesses = []
        wrongGuesses = list(wrongGuesses)

        wordLength = len(correctWord)
        for x in range(wordLength):
            guess.append("_")

        print(correctWord,guess,type(guess))
        wordGuess = "".join(str(element) for element in guess)

        while wordGuess != correctWord:
            clear()
            letter = ["T","O","O"," ","L","O","N","G"]
            print(f"- {wordGuess} -")
            print("\033[1;30;40m",end="")
            for x in wrongGuesses:  print(f"{x} ",end="")
            print(f"\033[0m")
            letter = str(input("What Letter Do you Guess? "))
            if len(letter) == 1:
                if letter in correctWord:
                    letterPos = [pos for pos, char in enumerate(correctWord) if char == letter]
                    for x in letterPos:
                        guess[x] = letter
                else: 
                    wrongGuesses.append(letter)
                wordGuess = "".join(str(element) for element in guess)
        print(f"You got it!\nThe word was {correctWord}!\nIt took you {len(wrongGuesses)} wrong guesses!")
    elif yn == "n":
        play = False
    else:
        print("Thats not a valid response...")