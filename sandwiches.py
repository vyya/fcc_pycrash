def make_sandwich(type, *ingridients):
    print(f'We use for {type} making, the following ingridients:')
    for ingridient in ingridients:
        print (f'- {ingridient}')

make_sandwich('hamburger', 'dough', 'beef', 'cucumber', 'salad')
make_sandwich('cheesburger', 'chees', 'chicken', 'tomato','cabbage')
make_sandwich('pita', 'minced meat', 'onion', 'garlic')
