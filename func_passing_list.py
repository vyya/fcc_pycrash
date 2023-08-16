# Passing alist of usernames to a function
def greet_users(names):
    for name in names:
        msg = f'Hello {name.title()}!'
        print(msg)
users = ['Naomi', 'Dan', 'Millie', 'George']
greet_users(users)