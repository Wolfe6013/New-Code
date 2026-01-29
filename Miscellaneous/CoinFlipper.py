import random, sys, os, time
NumberOfFlips: int = input("Number of flips to occur? ")
start = time.time()
done: int = 0
bestScore = 0
bestFlipHeads = True
heads = 0
tails = 0
consecutive = 0
flip = 2

for x, y in enumerate(range(int(NumberOfFlips))):
    side = random.randint(0,1)
    if y % 1000000 == 0 and y != 0:
        end = time.time()
        print(f"{y} - ({round(end - start,4)}sec, {round((end - start)/60,4)}min)")
    if side == 0:
        heads += 1
    else: tails += 1
    if side == flip:
        consecutive += 1
    else:
        if consecutive > bestScore:
            bestScore = consecutive
            if flip == 0:
                bestFlipHeads = True
            else:
                bestFlipHeads = False
        consecutive = 1
        flip = side

print(f"Heads was flipped `{heads}` times.\nTails was flipped `{tails}` times.")
if bestFlipHeads:
    print(f"Heads was flipped ",end="")
else:
    print(f"Tails was flipped ",end="")
print(f"{bestScore} times in a row.")

end = time.time()
print(f"It took {round(end - start,4)} seconds ({round((end - start)/60,4)}min) to finish.")