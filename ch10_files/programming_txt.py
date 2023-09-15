
from pathlib import Path

content = 'I love to talk to AI\n'
content += 'Let\'s talk over the interesting topic\n'
content += 'Bring me more interesting congent'

path = Path('programming.txt')
path.write_text(content)