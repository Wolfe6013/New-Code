import random

words = ["apple", "politics", "director", "autonomy", "council"]
chosenWord = random.choice(words)
chosenWordLength = -abs(len(chosenWord))

maxAttempts = 6
attempts = 0
calculatedAttempts = maxAttempts - attempts

while attempts < maxAttempts:
  print(f"You have {calculatedAttempts} attempt(s) left\n\n")

  if attempts < 1:
    length = abs(chosenWordLength)
    print("_ " * length, f"({length})")
  else:
    chosenWordLength += 1
    print(f"{chosenWord[0:chosenWordLength]} ", "_ " * abs(chosenWordLength))

  guess = input("Guess the Word: ")

  if guess == chosenWord:
    print(f"Winner! It was {chosenWord}!")
    print(f"You had {calculatedAttempts} attempt(s) left")

    exit(0)

  attempts += 1

print(f"You lost... the word was {chosenWord}")