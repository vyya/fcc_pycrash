from pathlib import Path
import json

def get_stored_username(path):
    """ Get stored username if available """
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """ Prompt new username"""
    username = input("Pleease enter your username: ")
    contents = json.dumps(username)
    path.write_text(contents)


def greet_user():
    """ Greet the user by name """
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f'Nice to see you again here {username}!')
    else:
        username = get_new_username(path)
        print(f'We\'ll remember you when you comes back next time {username}')

greet_user()