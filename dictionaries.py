# dictionaries
dog = {'name':'roger', 'age':8, 'color':'red'}
dog['name']='Greig' # replace name
print(dog['name'])
print(dog.get('name')) # get method
print(dog.get('color')) # get method
print(dog.get('color', 'brown')) # get method assigning value if missing
print(dog.pop('name')) # pop method returns and
# print(dog.popitem()) # retreat and remove last pair from the dictionary
print(dog)