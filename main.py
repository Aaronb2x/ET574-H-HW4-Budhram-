#Name: Aaron Budhram
#QCC ID: 24814218

import random

class Die:
    def __init__(self, sides=6, max_side=None):
        self.sides = max_side if max_side is not None else sides

    def roll(self):
        return random.randint(1, self.sides)
    

class DiceGame:
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()

    def evaluate_roll(self, total):
        if total in (7, 11):
            return "Win"
        elif total in (2, 3, 12):
            return "Lose"
        else:
            return "Roll Again"