import random

class Lottery:
    def __init__(self, series):
        self.series = series
    def choice(self, ticket):
        self.ticket = ticket
        selection = []
        n = 0
        while selection != self.ticket:
            selection = []
            for i in range(0, len(self.ticket)):
                pick = random.choice(self.series)
                selection.append(pick)
            n += 1
            print(f'Curent choice is {selection}, on attempt {n}')
        print(f'Your ticket matched this number {selection} and wins a prise on attempt {n}')

row = Lottery(['G', 'H', 3, 'L', 15, 2, 'P', 'X', 8])
row.choice(['L', 8, 'H', 3])  # Ensure that both lists have matching data types (strings)