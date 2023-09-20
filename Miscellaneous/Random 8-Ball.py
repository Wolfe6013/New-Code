import sys
import random
import time

def Question_Fetch(Response):

  answers = random.randint(1,5)

  QuestionSet = ["No","Yes","Maybe","Definitely Not","Definitely"]



  if Response == "":
      print("Shutting down...")
      sys.exit()

  else:

    return str(QuestionSet[answers-1]);



while True:

  question = input("What's your question? ")

  print(Question_Fetch(question))