import numpy as np


class QuantumGate:
   gates = {'X': np.array[
       [0, 1],
       [1, 0]],
       'H': np.array[
       [1, 1],
       [1, -1]],
       'CNOT': np.array[
       [1, 0, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 0, 1],
       [0, 0, 1, 0]
   ]
   }

   def __init__(self, type):
       self.type = type

   def compute(self, qubit):
       return qubit @ QuantumGate.gates[self.type]
