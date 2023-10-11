from pathlib import Path
import json

def get_stored_username(path):
    """ Get stored username is  exists """
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else: 
        return None
    

def get_new_username(path):

    username = {}
    while True:

        key = input(f'Enter a key (or type "exit" to stop):')
        if key.lower() == 'exit':
            break
        value = input(f'Enter a value: ')
        username[key] = value

    contents = json.dumps(username)
    path.write_text(contents)

def greet_user():

    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        
        print(f'Hello here is the username data:')
        for k,v in username.items():
            print(f'{k} - {v}')
    else:
        username = get_new_username(path)

greet_user()


