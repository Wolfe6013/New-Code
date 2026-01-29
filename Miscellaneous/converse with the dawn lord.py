import sys, random, time, os

def number_calculations(No):
  print(No/5)
  if No>=101: print('True')
  else: print('False')
  print(No % 9)
  if (No % 2) == 0: print ('Even')
  else: print ('Odd')
  print((5-No)+(1.5*No)/3)

while __name__ == "__main__":
  os.system("cls")
  No: int = input()
  number_calculations(int(No))
  input()