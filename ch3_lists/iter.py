names = ['eric', 'fedor', 'sam', 'eric', 'lana', 'gin', 'tom', 'lana', 'gleb']

to_remove = ['eric', 'gin', 'lana']
for item in to_remove:
        for name in names:
            if item == name:
                num = names.index(name)
                del names[names.index(name)]
                

        else:
           continue

print(names)