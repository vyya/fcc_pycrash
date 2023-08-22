def make_pizza(size, *toppings):
    """Print a list of toppings that have been requested"""
    print(f'Here is the list of the toppings have been requested:')
    for topping in toppings:
                print(f' size - {size} toppings - {topping}')
make_pizza('21"', 'pepperoni')
make_pizza('32"','cheese', 'tomatoes', 'rukkola')