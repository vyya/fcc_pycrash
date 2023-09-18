from pathlib import Path
import json

numbers = [2, 5, 8, 23, 43, 25]
path = Path('numbers.json')
contents = json.dumps(numbers)
#print(contents)
path.write_text(contents)