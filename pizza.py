def make_pizza(*toppings):
    """Print a list of toppings that have been requested"""
    print(f'Here is the list of the toppings have been requested:')
    for topping in toppings:
                print(f'- {topping}')
make_pizza('pepperoni')
make_pizza('cheese', 'tomatoes', 'rukkola')