oneDigit = 0
twoDigit = 0
threeDigit = 0
fourDigit = 0
fiveDigit = 0
sixDigit = 0
sevenDigit = 0
eightDigit = 0
nineDigit = 0
tenDigit = 0

for x, n in enumerate(range(999999)):
    n += 1
    if (n % 12) == 0:
        if (n % 11) == 0:
            if (n % 9) == 0:
                if (n % 9) == 0:
                    if (n % 8) == 0:
                        if (n % 7) == 0:
                            print(f"{n} - {int(n/2)} - {int(n/3)} - {int(n/4)} - {int(n/5)} - {int(n/6)} - {int(n/7)} - {int(n/8)} - {int(n/9)} - {int(n/10)}")
                            if n <= 9:
                                oneDigit += 1
                            elif n <= 99:
                                twoDigit += 1
                            elif n <= 999:
                                threeDigit += 1
                            elif n <= 9999:
                                fourDigit += 1
                            elif n <= 99999:
                                fiveDigit += 1
                            elif n <= 999999:
                                sixDigit += 1
                            elif n <= 9999999:
                                sevenDigit += 1
                            elif n <= 99999999:
                                eightDigit += 1
                            elif n <= 999999999:
                                nineDigit += 1
                            elif n <= 9999999999:
                                tenDigit += 1
print(f"{oneDigit}, {twoDigit}, {threeDigit}, {fourDigit}, {fiveDigit}, {sixDigit}, {sevenDigit}, {eightDigit}, {nineDigit}, {tenDigit}")