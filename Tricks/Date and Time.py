from datetime import datetime

now: datetime = datetime.now()
print(f'Date is: {now:%d/%m/%y (%H:%M:%S)}')
Day: int = f'{now:%d}'
Month: int = f'{now:%m}'
Year: int = f'{now:%y}'

print(f"{Day = }, {Month = }, {Year = }")