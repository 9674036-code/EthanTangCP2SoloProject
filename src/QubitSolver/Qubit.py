import numpy as np
class Qubit:
 def __init__(self, state):
     self.state = state
     self.gates=[]

 def compBasis(self):
     return f"0: {100*self.state[0]}% 1: {100*self.state[0]}%"
