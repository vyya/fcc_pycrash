from pathlib import Path

filenames = ['cat.txt', 'dog.txt', 'bat.txt']

for filename in filenames:
    path = Path(filename)
    try:
        content = path.read_text(encoding = 'utf-8')
    except:
        pass
       # print(f'File {path} not found')
    else:
        print(f'FIle {filename} content is \n {content}')

