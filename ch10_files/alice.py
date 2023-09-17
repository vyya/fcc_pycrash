from pathlib import Path

path = Path('alice.txt')
try:
    content = path.read_text(encoding = 'utf-8')
except:
    print(f'The file {path} does not exist. Enter a valid path')

else:
    # Counts the approximate number of words in the file
    words = content.split()
    
    num_words = len(words)
    print(f'The file {path} has about {num_words} words.')
