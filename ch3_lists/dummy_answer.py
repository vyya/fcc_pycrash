'''print('Generating dummy response!\n')
response = ''
while not response:# != 'because':
    response = input('Why?\n')
print('o\'kay')
input('\n\nPress the enter key to exit')'''
# Welcome player
greeting ='t\t\tGuess a random number game'
print(greeting.upper())
# Pick a random number between 1 and 100
import random
number = random.randint(1, 100)
# Ask the player for a guess
guess = int(input('\nPlease enter your guess number: '))
tries = 1
while guess != number:
    if guess > number:
        guess = int(input('\nPlease guess lower: '))
    else:
        guess = int(input('\nPlease guess higher: '))
    tries += 1
print('\nCongratulations!')
 
   
print(f'\nYour guess is correct on {tries} try! ')
input('\n\nPress Enter key to exit.')