import numpy as np
from functools import reduce

class QuantumGate:
 gates = {'X': np.array([
     [0, 1],
     [1, 0]]),
     'H': np.array([
         [1/np.sqrt(2), 1/np.sqrt(2)],
         [1/np.sqrt(2), -1/np.sqrt(2)]]),
     'CNOT': np.array([
     [1, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 1],
     [0, 0, 1, 0]
 ]),
     'Y': np.array([
         [0, -1j],
         [1j, 0]
     ]),
     'Z': np.array([
         [1, 0],
         [0, -1]
     ])
 }
 I=np.array([[1,0],[0,1]])
 def __init__(self, type, qubits):
     self.type = type
     self.qubits = qubits


 def compute(self, qubit, nQubits):
   gates=[]
   for i in range(nQubits):
       if i==self.qubits:
           gates.append(QuantumGate.gates[self.type])
       else:
           gates.append(QuantumGate.I)
   gate=reduce(np.kron,gates)
   return qubit @ gate
