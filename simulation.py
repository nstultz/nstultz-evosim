import numpy as np
import ujson

from generation import Generation

class Simulation():
    """Class representing the simulation as a whole"""
    def __init__(self, seed=None):
        # Generate the simulation seed
        self.seed = seed or np.random.randint(0, 2**32 - 1)
        np.random.seed(self.seed)
        # Set a place to store the generations in order
        self.generations = []
        # Set up the first generation
        self.cur_generation = Generation(count=0)
        self.generations.append(self.cur_generation)
    
    def export(self):
        return ujson.dumps(self)
