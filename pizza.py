def make_pizza(size, *toppings):
    """Print a list of toppings that have been requested"""
    print(f'Here is the list of the toppings have been requested:')
    n = 1
    for topping in toppings:
                print(f'{n}-size-{size} - {topping}')
                n = n + 1
make_pizza(16, 'pepperoni')
make_pizza(32, 'cheese', 'tomatoes', 'rukkola')