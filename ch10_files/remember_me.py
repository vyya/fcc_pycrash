from pathlib import Path
import json

username = input('Please enter your username: ')
path = Path('username.json')
content = json.dumps(username)
path.write_text(content)
print(f'We\'ll remember you when you comes back next time {username}')