import sys
import random
import time

def Question_Fetch(Response):

  CohenAnswers = random.randint(1,20)
  CharlieAnswers = random.randint(1,20)
  
  if CohenAnswers == CharlieAnswers:
      CharlieAnswers = CharlieAnswers-1
      
  else:
      
      Charlie = ["Astra!","Breach!","Brimstone!","Chamber!","Cypher!","Fade!","Harbour!","Jett!","KAY/O!","Killjoy!","Neon!","Omen!","Pheonix!","Raze!","Reyna","Sage!","Skye!","Sova!","Viper!","Yoru!"]
      Cohen = ["Astra!","Breach!","Brimstone!","Chamber!","Cypher!","Fade!","Harbour!","Jett!","KAY/O!","Killjoy!","Neon!","Omen!","Pheonix!","Raze!","Reyna","Sage!","Skye!","Sova!","Viper!","Yoru!"]
  
  if Response == "n":
      print("Nothing, duh!")
      sys.exit()

  else:

    return str(Charlie[CohenAnswers-1]);
    return str(Cohen[CharlieAnswers-1]);

while True:
  question = input("Agent? (y/n) ")
  print()
  print("Charlie got... ")
  print(Question_Fetch(question))
  print()
  print("Cohen got... ")
  print(Question_Fetch(question))
  print()