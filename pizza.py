def make_pizza(size, *toppings):
    """Print a list of toppings that have been requested"""
    print(f'Making a {size}-inch pizza with the following topings:')

    for topping in toppings:
        print(f'toppings - {topping}')

