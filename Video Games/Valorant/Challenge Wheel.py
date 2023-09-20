import sys
import random
import time

def Question_Fetch(Response):
  ChallengeAnswers = random.randint(1,23)
  Challenge = ["Knife Only","Side-arm Only","No Volume","Shotgun Only","No Crosshair","Sense Max","Sense Min","Narrator","Sniper Only","FPS 25","No Shields","Inverted Mouse","Minimap Off","HUD Off","Unbind Walk Forward","W=S, A=D","Request Force","Bot Player","No Util","Thicc Crosshair and Reroll","One-Bullet","Random Agent","Full Rush"]
  if Response == "n":
      print("Nothing, duh!")
      sys.exit()

  else:

    return str(Challenge[ChallengeAnswers-1]);

while True:
  question = input("Run? (y/n) ")
  print()
  print("Your Challenge is... ")
  print(Question_Fetch(question))
  print()