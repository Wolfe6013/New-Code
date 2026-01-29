foundValues = []
factorsList = []
composite = 1
for x in range(25):
    factorsList.append((x+1))
    found = False
    while not found:
        successful = True
        for factor in factorsList:
            if composite % (factor) != 0:
                successful = False
        if successful:
            found = True
        else:
            composite += 1
    foundValues.append(composite)
    print(f"{composite} - {factorsList}")
print(foundValues)