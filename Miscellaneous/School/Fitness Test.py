def Calculate():
    Leave = 0
    if sex == 'M' or sex == 'm' or sex == 'F' or sex == 'f':
        if sex == 'M' or sex == 'm':
            SexNumber = 6.315
        else:
            SexNumber = 0
        Weightlb = WeightKG*2.205
    else:
        print(f"Bad Rabbit! \n{sex}isn't a M or F")
        Leave = 1
    if Leave == 0:
        print(132.853-(0.0769*Weightlb)-(0.3877*age)+SexNumber-(3.2649*time)-(0.1565*heartrate))
confirm = 'N'
while confirm != 'Y':
    WeightKG = float(input('What is your weight (in kg) '))
    age = int(input('What is your age (in years) '))
    sex = input('What is your sex (M/F) ')
    time = int(input('How long did it take you to complete the one mile walk (in min) '))
    heartrate = int(input('What was your heartrate in the final two minutes (bpm) '))
    print(f'Is this correct:\nWeight = {WeightKG}\nAge = {age}\nSex = {sex}\nTime Taken = {time}\nHeartrate = {heartrate}\nIs this correct? (Y/N)')
    confirm = input()
    if confirm == 'Y':
        Calculate()
    else:
        print(f'Bad Rabbit!')