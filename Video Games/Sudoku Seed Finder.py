import random
done = 0
boxChoices = [' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3','4','5','6','7','8','9']

finalSeed = []
splt = 0

while splt < 81:
    while done < 81:
        done+=1
        seedDigit = 0
        finalSeed.append(random.choice(boxChoices))
    for x in boxChoices:
        if x in finalSeed:
            splt += 1
            
            

for x in finalSeed:
    print(x, end-'')