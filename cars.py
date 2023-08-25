def make_car(manufacturer, model, **info):
    info['brand_name'] = manufacturer
    info['model_name'] = model
    return info

car = make_car('Subaru', 'Outback', color = 'magenta', gear = 'automatic', tow_package = True)
print(car)