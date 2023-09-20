import time

print('Options:')
print('AnswerFast()  -  Give you only the number of runs, very fast')
print('InfoFast()    -  Give you number after each run, fast')
print('InfoSlow() -  Give you number after each run, and delay so you can read it, 0.2 seconds between numbers')
print('All will apply the following formula until no = 1 (because it infinately repeats, 1*3+1 = 4/2 = 2/2 = 1):')
print('if (no) = Even then no = no/2')
print('if (no) = Odd then no = no*3+1')

def AnswerFast(first):
    runno = 0
    during = first
    while during != 1:
        #print(during)     -just info
        if (during % 2) == 0: during = during/2
        else: during = (during*3)+1
        #time.sleep(0.2)     -makes info readable
        runno = runno+1
    #print(during)     -just info
    print(first,'reached',during,'after',runno,'runs!')
    
def InfoFast(one):
    runno = 0
    during = one
    while during != 1:
        print(during)
        if (during % 2) == 0: during = during/2
        else: during = (during*3)+1
        #time.sleep(0.2)     -makes info readable
        runno = runno+1
    print(during)
    print(one,'reached',during,'after',runno,'runs!')
    
def InfoSlow(primary):
    runno = 0
    during = primary
    while during != 1:
        print(during)
        if (during % 2) == 0: during = during/2
        else: during = (during*3)+1
        time.sleep(0.2)
        runno = runno+1
    print(during)
    print(primary,'reached',during,'after',runno,'runs!')