# some designs that need to be printed
unprinted_design = ['phone case', 'remote control', 'robot pendant', 'dodecahedron']
completed_models = []

# simulate printing each design until none are left
# adding printed design to completed models after printing
def printed_models(unprinted_design, completed_models):
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f'Printing model: {current_design}')
        completed_models.append(current_design)

def show_completed_models(completed_models):
    for model in completed_models:
        print(model)

unprinted_design = ['phone case', 'remote control', 'robot pendant', 'dodecahedron']
completed_models = []

printed_models(unprinted_design[:], completed_models)
show_completed_models(completed_models)
print(unprinted_design)
        