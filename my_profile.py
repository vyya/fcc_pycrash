def build_profile(first, second, **my_info):
    my_info['first_name'] = first
    my_info['last_name'] = second
    return my_info

my_data = build_profile('John', 'Malkovich', spetiality = 'pythonist', character = 'nordic', mentality = 'liberal')
print(my_data)