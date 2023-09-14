from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()
content = content.replace('Python', 'C++')
print(content)
"""lines = content.splitlines()
print(lines)"""
# content.split_lines() not assigned to a variable
for line in content.splitlines(): 
    line = line.replace('Python', 'C++')
    print(line)