from Qubit import Qubit
import numpy as np
from QuantumGate import QuantumGate
import pygame
from functools import reduce
pygame.init()


class QuantumCircut:
   levels = {1: [np.array([1, 0])], 2: [np.array([1,0]), np.array([0,1]),np.array([1,0])]}
   def __init__(self, level):
       self.level = level
       self.qubits = []
       self.gates={}
       self.box=[]
       for i in QuantumCircut.levels[level]:
           self.qubits.append(Qubit(i))
       states = [i.state for i in self.qubits]
       self.qSystem=reduce(np.kron,states)
       self.nQSystem=self.qSystem
       print(self.qSystem)




   def update(self, level):
       self.level = level
       self.qubits = []
       for i in QuantumCircut.levels[level]:
           self.qubits.append(Qubit(i))




   def display(self, surface, font):
       self.nQSystem=self.qSystem
       for i in self.gates:
           self.nQSystem=self.gates[i].compute(self.nQSystem,len(self.qubits))
       t = 550//(len(QuantumCircut.levels[self.level])+1)
       self.box=[]
       for i in range(1, len(QuantumCircut.levels[self.level])+1):
           pygame.draw.line(surface, (240, 240, 240), (200, i*t), (930, i*t), 5)
           if i==1:
               text = font.render(f"|\u03C8>", True, (255, 255, 255))
           else:
               text = font.render(f"|{(self.qubits[i-1].state[0])^1}>", True, (255, 255, 255))
           surface.blit(text, (150, i*t-20))
           self.box.append((200,i*t))




   def compBasis(self):
       return self.qubits[0].compBasis()
 
   def addGate(self, gate, qNum):
       self.gates.setdefault(qNum,QuantumGate(gate, qNum))
       print(self.gates)
       self.qubits[qNum].gates.append(gate)