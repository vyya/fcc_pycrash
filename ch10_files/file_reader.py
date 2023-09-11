from pathlib import Path

path = Path('text_files/pi_digits.txt')
content = path.read_text().rstrip()
print(content)
