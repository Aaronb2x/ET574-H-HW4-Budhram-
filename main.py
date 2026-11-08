#Name: Aaron Budhram
#QCC ID: 24814218

import random

class Die:
    def __init__(self, sides=6, max_side=None):
        self.sides = max_side if max_side is not None else sides

    def roll(self):
        return random.randint(1, self.sides)
    