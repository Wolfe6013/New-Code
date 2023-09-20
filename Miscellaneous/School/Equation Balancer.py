reactantAmount = int(input('How many reactants is there? ')) ###if the element has only one letter, oxygen, write O_)
productAmount = int(input('How many products is there? ')) ###for each element put the subscript normally (put 1 if no sub)
allReactants = []
reactantsSplit = []
allProducts = []
productsSplit = []
finalReactant = []
finalProduct = []
relativePos = 1
listPos = 0

while reactantAmount > 0:
    reactantCurrent = input('What is the reactant? ')
    reactantAmount -= 1
    allReactants.append(reactantCurrent)

while productAmount > 0:
    productCurrent = input('What is the product? ')
    productAmount -= 1
    allProducts.append(productCurrent)

for x in allReactants:
    for y in x:
        if relativePos == 1:
            print(x[listPos])
            print(x[listPos+1])
            print(x[listPos+2])
            checkedReaction = [y,x[listPos+1]]
            finalReactant.append(checkedReaction)
            finalReactant.append(x[listPos+2])
        if relativePos == 3:
            relativePos = 0
        relativePos += 1
        listPos += 1

for x in finalReactant:
    print(x)

for x in finalProduct:
    print(x)