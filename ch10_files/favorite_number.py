from pathlib import Path
import json

number = input("Please input your favorite number: ")
path = Path('number.json')
contents = json.dumps(number)
path.write_text(contents)