from pathlib import Path

path = Path('text_files/pi_digits.txt')
content = path.read_text()

lines = content.splitlines()
for line in lines:
    print(line)
