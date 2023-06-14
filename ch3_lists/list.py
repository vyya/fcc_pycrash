friends = ['max', 'vic', 'saken', 'alex', 'anton']
print(f"{friends[-1].title()}")
# print(dir(friends))
friends.append('sanya')
print(friends)
friends.insert(1, 'sholpa')
print(friends)
friends.remove('vic')
print(friends[:-2])
relatives = []
relatives.append('wife')
relatives.append('son')
print(relatives[0].upper())
del friends[0]
del friends[0]
print(friends)
friends.append('john')
popped_friend = friends.pop()
print(friends)
print(popped_friend)
best_friend = friends.pop(1)
print(f'My best friend was {best_friend.title()}')
no_more ='sanya'
friends.remove(no_more)
print(f'\t{no_more.title()} is not my friend anymore')
print(friends)