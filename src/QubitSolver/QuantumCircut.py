from Qubit import Qubit
import numpy as np
from QuantumGate import QuantumGate
import pygame
from functools import reduce
pygame.init()


class QuantumCircut:
   levels = {1: [np.array([1, 0])], 2: [np.array(
       [0, 1])], 3: [np.array([1/np.sqrt(2), 1/np.sqrt(2)])], 4: [np.array([1/np.sqrt(2), -1/np.sqrt(2)])], 5: [np.array([np.cos(np.pi/12), np.sin(np.pi/12)])]}

   def __init__(self, level):
       self.level = level
       self.qubits = []
       self.gates = {}
       self.box = []
       for i in QuantumCircut.levels[level]:
           self.qubits.append(Qubit(i))
       states = [i.state for i in self.qubits]
       self.qSystem = reduce(np.kron, states)
       self.nQSystem = self.qSystem

   def update(self, level):
       self.level = level
       self.qubits = []
       for i in QuantumCircut.levels[level]:
           self.qubits.append(Qubit(i))

   def display(self, surface, font):
       self.nQSystem = self.qSystem
       t = 550//(len(QuantumCircut.levels[self.level])+1)
       self.box = []
       for i in range(1, len(QuantumCircut.levels[self.level])+1):
           pygame.draw.line(surface, (240, 240, 240),
                            (200, i*t), (890, i*t), 5)
           if i == 1:
               text = font.render(f"|\u03C8>", True, (255, 255, 255))
               #surface.blit(text, (900, i*t-20)) --- IGNORE --- Potential additional feature
           else:
               text = font.render(
                   f"|{(self.qubits[i-1].state[0]) ^ 1}>", True, (255, 255, 255))
           surface.blit(text, (150, i*t-20))
           self.box.append((200, i*t))

   def compBasis(self):
       self.calculate()
       return self.qubits[0].compBasis(self.nQSystem)

   def addGate(self, gate, qNum):
       self.gates.setdefault(qNum, []).append(QuantumGate(gate, qNum))
       self.qubits[qNum].gates.append(gate)

   def calculate(self):
       for i in self.gates:
        for i2 in self.gates[i]:
            self.nQSystem = i2.compute(
                self.nQSystem, len(self.qubits))
