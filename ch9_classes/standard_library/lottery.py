import random

class Lottery:
    def __init__(self, series):
        self.series = series
    def choice(self):
        selection = []
        for i in range(0, 4):
            pick = random.choice(self.series)
            selection.append(pick)
        print(f'Ticket matching this number {selection} wins a prise')

row = Lottery(['G', 'H', 3 , 'L', 15, 2, 'P', 'X', 8, 'n', 'T', 's', 'M', 'a'])
row.choice()

