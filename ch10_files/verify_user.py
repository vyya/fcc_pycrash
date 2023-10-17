from pathlib import Path
import json 

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(path):

    username = {}
    while True:
        key = input(f'Please enter a key(or type "exit" to stop):')
        if key == 'exit':
            break
        else:
            value = input(f'Please enter a value:')
            username[key] =  value

        contents = json.dumps(username)
        path.write_text(contents)

def greet_user():

    path = Path('username.json')
    username = get_stored_username(path)
    
    if username:
        for k,v in username.items():
                print(f'{k} - {v}')
        answer = input(f'Is this a correct username. Please type "yes" or "no"\
: ')
        if answer == 'no':
            get_new_username(path)
        else:
            print(f'Welcome back, dear user:')
            for k,v in username.items():
                print(f'{k} - {v}')
            
                      
    else:
        get_new_username(path)

greet_user()
