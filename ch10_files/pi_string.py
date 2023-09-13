from pathlib import Path

path = Path('pi_digits.txt')
content = path.read_text()
lines = content.splitlines()
print(lines)
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(pi_string)
print(len(pi_string))