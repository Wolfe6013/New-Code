import sys
import random
import time

def Question_Fetch(Response):

  answers = random.randint(1,7)

  Cohen = ["Brimstone","Jett","Pheonix","Sage","Sova","Fade","Kayo"]


  if Response == "n":
      print("Shutting down...")
      sys.exit()

  else:

    return str(Cohen[answers-1]);



while True:

  question = input("Agent? (y/n) ")

  print(Question_Fetch(question))