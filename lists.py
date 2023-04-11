dogs = ['Roger', 'Syd','QUincy']
dogs[2] = 'Martin'
dogs.append('Archie') # append one item to the list 
dogs.extend(['Great', 'Flask']) # extend one list with  another
dogs += ['MAth', 'Flat'] # extension with +=
dogs.remove('Syd') # remove method
print(dogs.pop()) # remove last item from the list and return it
print(dogs)
dogs.insert(1, 'inserted') # insert item on a certain position
dogs[2:2] = ['slicer', 'dicer'] # insert multiple items using slicer
print(sorted(dogs, key=str.lower))
print(dogs)
dogscopy = dogs[:] # making a copy of the whole list
dogs.sort(key=str.lower, reverse=True) # sorting, str.lower ignores the case of string 
print(dogs)
print(dogscopy)
