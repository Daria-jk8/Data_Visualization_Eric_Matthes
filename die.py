from random import randint
 
class Die():

    def __init__(self, num_sides=6):
        # --> The default hexagon cube is used
        self.num_sides = num_sides 


    def roll(self):
        # --> Random return of a number from 1 to num_sides
        return randint(1, self.num_sides)