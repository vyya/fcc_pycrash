from pathlib import Path

guest = None
guests = ''
while guest != '':
    guest = input('Please enter your name:')
    guests += f"{guest}\n"

path = Path('guests.txt') 
path.write_text(guests)

