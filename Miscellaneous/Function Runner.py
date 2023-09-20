def Function():
    print("I'm a function!")

def FunctionList():
    print('The functions are as follows:')
    Functions = ['Function()']
    for x in Functions:
        print(x)
    print()
    WhichFunction = input()
    print()
    found = 0
    if WhichFunction == 'Function()':
        found = 1
        Function()
    if found == 0:
        print('No function found with that specifications.')
FunctionList()