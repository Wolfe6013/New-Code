import sys
import random
import time

def Question_Fetch(Response):

  ChallengeAnswers = random.randint(1,15)
  Challenge = ["Brimstone!","Chamber!","Cypher!","Jett!","KAY/O!","Neon!","Omen!","Pheonix!","Raze!","Reyna","Sage!","Skye!","Sova!","Viper!","Yoru!"]
  
  if Response == "n":
      print("Nothing, duh!")
      sys.exit()

  else:

    return str(Challenge[ChallengeAnswers-1]);

while True:
  question = input("Run? (y/n) ")
  print()
  print("Jake's Agent is... ")
  print(Question_Fetch(question))
  print()
