guests = ['merilin', 'buzz', 'hugo', 'alt']
print(f'You\'re shiny, {guests[0].title()}')
print(f'Big step, {guests[1].title()}!')
print(f'Like a boss, {guests[2].title()}!')
print(f'Good to see you, {guests[-1].title()}')
sick_out = guests.pop(3)
print(f'Inadvertently {sick_out.title()} could not make a dinner')
new_invited = guests.insert(3, 'liz')
print(f'You\'re shiny, {guests[0].title()}')
print(f'Big step, {guests[1].title()}!')
print(f'Like a boss, {guests[2].title()}!')
print(f'Good to see you, {guests[-1].title()}')
print('\nWe\'ve found a bigger table and we\'re inviting more\n')
guests.insert(0, 'Alan')
guests.insert(int(len(guests)/2), 'Adriano')
guests.append('lilly')
print(guests)
print(f'You\'re shiny, {guests[0].title()}')
print(f'Big step, {guests[1].title()}!')
print(f'Like a boss, {guests[2].title()}!')
print(f'Good to see you, {guests[-1].title()}')