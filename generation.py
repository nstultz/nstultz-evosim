import numpy as np

from candidate import Candidate

class Generation():
    """Represents one generation of the simulation"""
    def __init__(self, count=0, survivors=None):
        # Set the generation counter
        self.count = count
        # Get the candidates for this generation
        if survivors:
            # If this is not the first generation, we take the survivors and generate children
            self.candidates = [Candidate(dup=cand) for cand in survivors] + [Candidate(parent=cand) for cand in survivors]
        else:
            # Otherwise we generate a set of brand new candidates
            self.candidates = [Candidate() for _ in range(100)]
