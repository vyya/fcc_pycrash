from pathlib import Path
import json

path = Path('number.json')
contents = path.read_text()
number = json.loads(contents)

print(f'I know your favorite number. It is {number}')
