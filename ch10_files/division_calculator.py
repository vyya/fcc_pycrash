print('Simple division calculator program')
print('Press \'q\' to quit')
while True:

    first_number = (input('Please enter first number:'))
    if first_number == 'q':
        break
    second_number = (input('Please enter the second number:'))
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except:
        print('Input numbers only')
    else:
        print(answer)

        