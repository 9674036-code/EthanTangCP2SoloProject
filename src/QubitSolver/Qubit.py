import numpy as np
class Qubit:
 def __init__(self, state):
     self.state = state

 def compBasis(self):
     return f"{np.random.choice([0, 1], p=[self.state[0],self.state[1]])}"