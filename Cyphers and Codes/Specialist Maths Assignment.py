from GroupDecend import Encode, Decode
from Matrix import input

if __name__ == "__main__":
    UserInput: str = input("> ")
    EncodedInput = Encode(UserInput)
    print(f"{EncodedInput}\n")
    DecodedInput = Decode(EncodedInput)
    print(f"{DecodedInput}\n")