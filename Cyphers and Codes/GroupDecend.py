#Hello there! I am very pleased to be of your acquaintance.  #original message
#leH oleht!er I ma revp yaeldesot eb fo oy  ruqcaiauatnecn  .#Every three is turned into groups and inverted
#o Hel!thel I reer amay pvsedlebe too of ur  yaiacqentau.  nc#Every five
#t!leH or I lehama reedesvp yot ebelru fo ocaiay  .uatneq  cn   #Every seven

def Invert(Text: str,Size: int):
    NormalList: list = []
    x: int = Size - (len(Text) % Size)
    if x < Size:
        for y in range(x):
            Text = Text + "?"
    for Position, Letter in enumerate(Text):
        if Position%Size == 0:
            NormalList.append(f"{Text[Position]}{Text[Position+1]}{Text[Position+2]}")
    EncodedList: list[str] = []
    for x in NormalList:
        print(x[::-1])
        EncodedList.append(x[::-1])
    EncodedText: str  = ''.join(EncodedList)
    return EncodedText

def Encode(Text: str):
    StepOne: str = Invert(Text,3)
    StepTwo: str = Invert(StepOne,5)
    StepThree: str = Invert(StepTwo,7)
    return StepThree

def Decode(Text: str):
    StepOne: str = Invert(Text,7)
    StepTwo: str = Invert(StepOne,5)
    StepThree: str = Invert(StepTwo,3)
    return StepThree

if __name__ == "__main__":
    UserInput: str = input("> ")
    EncodedInput = Encode(UserInput)
    print(f"{EncodedInput}\n")
    DecodedInput = Decode(EncodedInput)
    print(f"{DecodedInput}\n")
