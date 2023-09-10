
import random
class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        for i in range(1, 11):
            side = random.randint(1, self.sides)
            print(f'Dice roll #{i} - We v got die {side}')

roll_20 = Die(20)
roll_20.roll_die()
roll_10 = Die(10)
roll_10.roll_die()