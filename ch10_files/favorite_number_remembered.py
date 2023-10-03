from pathlib import Path
import json

def get_remembered_num(path):
    """ Get remembered number if available """
    if path.exists():
        contents = path.read_text()
        number = json.loads(contents)
        return number
    else:
        return None
    
def get_favorite_number(path):
    """ Get new number and write it to a json file """
    number = input(f'Please input your favorite number: ')
    contents = json.dumps(number)
    path.write_text(contents)

def tell_number():
    """ Tell the number if exists """
    path = Path('number.json')
    number = get_remembered_num(path)
    if number:
        print(f'I know your favorite number. It is {number}')
    else:
        number = get_favorite_number(path)

tell_number()