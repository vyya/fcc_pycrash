from pathlib import Path

path = Path('alice.txt')
try:
    content = path.read_text(encoding = 'utf-8')
except:
    print(f'The file {path} does not exist. Enter a valid path')

