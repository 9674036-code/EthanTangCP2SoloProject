import numpy as np

class Qubit:
 def __init__(self, state):
     self.state = state
     self.nState=state
     self.gates = []

 def compBasis(self, system):
    matrix=system.reshape(2,-1)
    u,s,vh=np.linalg.svd(matrix)
    self.nState=u[:,0]
    return f"0: {round(100*np.square(np.abs(self.nState[0])))}% 1: {round(100*np.square(np.abs(self.nState[1])))}%"
