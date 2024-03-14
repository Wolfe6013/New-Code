total: int = 0

while True:
    user_input: str = input('Add: ')

    try:
        total += int(user_input)
    except ValueError:
        try:
            total += float(user_input)
        except:
            print('Please enter a valid number...')
    except Exception as e:
        print(repr(e))
    
    print(f'Current: {total:,}')