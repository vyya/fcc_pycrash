from pathlib import Path

user_name = input('Please enter your username:')

path = Path('guest.txt')
path.write_text(user_name)
