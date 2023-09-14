from pathlib import Path

path = Path('pi_million_digits.txt')
content = path.read_text()
lines = content.splitlines()

pi_string = ''
for line in lines:
    pi_string += line.lstrip()
birthday = input('Please input your birthday in format "ddmmyy":')
if birthday in pi_string:
    print(f'\nYour birthday {birthday} appear in the pi digit\n')
else:
    print(f'Your birthday doesn\'t appear in the pi digit')
print(f'{pi_string[:52]}')
print(len(pi_string))