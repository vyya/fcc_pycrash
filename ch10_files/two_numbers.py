# Two numbers edition
result = None
while result == None:
    number1 = input(f'\nPlease enter the first number: ')
        
    number2 = input('\nPlease enter a second number: ')

# results output

    try:
        result = int(number1) + int(number2)
    except:
        print('\nInput numbers only')
    else:
        print(f'\nResult of addition of two numbers is: {result}')