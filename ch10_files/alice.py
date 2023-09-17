from pathlib import Path

def count_words(path):
                               
    
        try:
            content = path.read_text(encoding = 'utf-8')
        except:

            # print(f'The file {path} does not exist. Enter a valid path')
            pass

        else:
            # Counts the approximate number of words in the file
            words = content.split()
            
            num_words = len(words)
            print(f'The file {path} has about {num_words} words.')

filenames = [
            'alice.txt', 
            'sidhartha.txt',
            'moby_dick.txt',
            'little_women.txt'            
            ]

for filename in filenames:
    path = Path(filename)
    count_words(path)