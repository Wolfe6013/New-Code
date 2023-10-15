import random

Full_Deck = ["Ace of Hearts","Ace of Clubs","Ace of Spades","Ace of Diamonds","2 of Hearts","2 of Clubs","2 of Spades","2 of Diamonds","3 of Hearts","3 of Clubs","3 of Spades","3 of Diamonds","4 of Hearts","4 of Clubs","4 of Spades","4 of Diamonds","5 of Hearts","5 of Clubs","5 of Spades","5 of Diamonds","6 of Hearts","6 of Clubs","6 of Spades","6 of Diamonds","7 of Hearts","7 of Clubs","7 of Spades","7 of Diamonds","8 of Hearts","8 of Clubs","8 of Spades","8 of Diamonds","9 of Hearts","9 of Clubs","9 of Spades","9 of Diamonds","10 of Hearts","10 of Clubs","10 of Spades","10 of Diamonds","Jack of Hearts","Jack of Clubs","Jack of Spades","Jack of Diamonds","Queen of Hearts","Queen of Clubs","Queen of Spades","Queen of Diamonds","King of Hearts","King of Clubs","King of Spades","King of Diamonds"]
Numbered_Deck = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]

Modified_Full_Deck = ["Ace of Hearts","Ace of Clubs","Ace of Spades","Ace of Diamonds","2 of Hearts","2 of Clubs","2 of Spades","2 of Diamonds","3 of Hearts","3 of Clubs","3 of Spades","3 of Diamonds","4 of Hearts","4 of Clubs","4 of Spades","4 of Diamonds","5 of Hearts","5 of Clubs","5 of Spades","5 of Diamonds","6 of Hearts","6 of Clubs","6 of Spades","6 of Diamonds","7 of Hearts","7 of Clubs","7 of Spades","7 of Diamonds","8 of Hearts","8 of Clubs","8 of Spades","8 of Diamonds","9 of Hearts","9 of Clubs","9 of Spades","9 of Diamonds","10 of Hearts","10 of Clubs","10 of Spades","10 of Diamonds","Jack of Hearts","Jack of Clubs","Jack of Spades","Jack of Diamonds","Queen of Hearts","Queen of Clubs","Queen of Spades","Queen of Diamonds","King of Hearts","King of Clubs","King of Spades","King of Diamonds"]
Modified_Numbered_Deck = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]

#Draw

def CalculateChances(NumList,CardList):
    Average = 0
    for x in NumList:
        Average += x
    Average = Average / len(NumList)
    print(f"{len(CardList)} cards left in deck, with an average of {Average}.")

while True:
    CardRemoved = input("Name of Card Removed: ")
    found = 0
    if CardRemoved == "Average":
        CalculateChances(Modified_Numbered_Deck,Modified_Full_Deck)
        found = 1

    if CardRemoved == "Shuffle":
        Modified_Full_Deck = Full_Deck
        Modified_Numbered_Deck = Numbered_Deck
        found = 1

    if CardRemoved == "Reveal":
        for x in Modified_Full_Deck:
            print(f"{x}")
        found = 1

    if CardRemoved == "Draw":
        RandomCard = random.choice(Modified_Full_Deck)
        print(f"{RandomCard}. There is {len(Modified_Full_Deck)-1} cards left. You need to write it in.")
        CardPos = Modified_Full_Deck.index(RandomCard)
        Modified_Full_Deck.pop(CardPos)
        Modified_Numbered_Deck.pop(CardPos)
        if CardPos <= 3:
            Modified_Numbered_Deck.pop(len(Modified_Numbered_Deck)-1)
        found = 1

    if CardRemoved in Modified_Full_Deck:
        CardPos = Modified_Full_Deck.index(CardRemoved)
        Modified_Full_Deck.pop(CardPos)
        Modified_Numbered_Deck.pop(CardPos)
        if CardPos <= 3:
            Modified_Numbered_Deck.pop(len(Modified_Numbered_Deck)-1)
        found = 1
    
    if found == 0:
        if CardRemoved in Full_Deck:
            print(f"Card, '{CardRemoved}', not in deck (it was removed).")
        else:
            print(f"Card, '{CardRemoved}', not in deck (it isn't a card).")