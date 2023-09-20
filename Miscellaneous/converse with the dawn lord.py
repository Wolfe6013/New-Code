import sys
import random
import time

No = 0
def number_calculations(No):
  print(No/5)
  if No>=101: print('True')
  else: print('False')
  print(No % 9)
  if (No % 2) == 0: print ('Even')
  else: print ('Odd')
  print((5-No)+(1.5*No)/3)