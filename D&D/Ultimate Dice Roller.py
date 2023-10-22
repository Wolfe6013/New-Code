import random
import time
import sys
import math

def Exit():
    sys.exit()

def d(Type,Mod):
    Roll = random.randint(1,Type)
    print(Roll+Mod)

def m(TotalDone,Type):
    TimesDone = 0
    TotalAmount = 0
    while TimesDone < TotalDone:
        Roll = random.randint(1,Type)
        print(Roll)
        TotalAmount = TotalAmount+Roll
        TimesDone = TimesDone+1
    print('Total is',TotalAmount)
    
def Advantage(Mod):
    Roll1 = random.randint(1,20)
    Roll2 = random.randint(1,20)
    print('Dice One rolled',Roll1)
    print('Dice Two rolled',Roll2)
    if Roll1 > Roll2: print(Roll1+Mod)
    else: print(Roll2+Mod)
    
def Disadvantage(Mod):
    Roll1 = random.randint(1,20)
    Roll2 = random.randint(1,20)
    print('Dice One rolled',Roll1)
    print('Dice Two rolled',Roll2)
    if Roll1 < Roll2: print(Roll1+Mod)
    else: print(Roll2+Mod)

def Fireball(Upcast):
    TimesDone = 0
    TotalAmount = 0
    while TimesDone < 8+Upcast:
        Roll = random.randint(1,6)
        TotalAmount = TotalAmount+Roll
        TimesDone = TimesDone+1
        print(Roll,'to a total of',TotalAmount)
    HalfDamage = math.ceil(TotalAmount/2)
    print(TotalAmount,'fire damage on a failed save, and',HalfDamage,'on a success.')
    
def AnimateObjects(Upcast):
    TimesDone = 0
    TotalAmount = 0
    TotalMisses = 0
    AC = int(input('Enemy AC? '))
    while TimesDone < 10+(Upcast*2):
        TimesDone = TimesDone+1
        Roll = random.randint(1,20)
        print('Coin',TimesDone,'got a',Roll+8,'to hit.')
        if Roll+8 < AC:
            TotalMisses = TotalMisses+1
    TimesDone = 0
    print(TotalMisses,'missed out of',10+(Upcast*2))
    while TimesDone < 10+(Upcast*2)-TotalMisses:
        TimesDone = TimesDone+1
        Roll = random.randint(1,4)
        TotalAmount = TotalAmount+Roll+4
        print('Coin (hit)',TimesDone,'deals',Roll+4,'bludgeoning damage! Current total is',TotalAmount)
    print('To a total of',TotalAmount,'bludgeoning damage.')
    
def IceKnife(Modifier,Upcast):
    EnemyAC = int(input('Enemy AC? '))
    TimesDone = 0
    TotalAmount = 0
    Hit = random.randint(1,20)
    print(Hit+Modifier,'to hit.')
    if Hit+Modifier >= EnemyAC:
        print('That hits!')
        d10 = random.randint(1,10)
        print(d10,'damage')
    else:
        print('That misses!')
    while TimesDone < 2+Upcast:
        Roll = random.randint(1,6)
        TotalAmount = TotalAmount+Roll
        TimesDone = TimesDone+1
        print(Roll,'to a total of',TotalAmount)
    HalfDamage = math.ceil(TotalAmount/2)
    if Hit+Modifier >= EnemyAC:
        print(d10,'piercing damage plus')
    else:
        time.sleep(0)
    print(TotalAmount,'cold damage on a failed save, and',HalfDamage,'on a success.')

def Skeletons():
    print('Calculating for 35 skeletons')
    EnemyAC = int(input('What is the enemy ac? '))
    TimesDone = 0
    TotalDamage = 0
    while TimesDone < 35:
        TimesDone = TimesDone+1
        ToHit = random.randint(1,20)
        print('Skeleton',TimesDone,'got a',ToHit+4,'to hit')
        if ToHit+4 >= EnemyAC:
            Damage = random.randint(1,6)
            if ToHit == 20:
                print('Skeleton',TimesDone,'deals',Damage*2+12,'piercing damage')
                TotalDamage = TotalDamage+Damage*2+12
            else:
                print('Skeleton',TimesDone,'deals',Damage+6,'piercing damage')
                TotalDamage = TotalDamage+Damage+6
    print('To a total of',TotalDamage,'piercing damage')

Skeletons()
AnimateObjects(0)
Fireball(0)