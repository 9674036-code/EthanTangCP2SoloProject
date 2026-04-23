
from Qubit import Qubit
import numpy as np
import pygame
from functools import reduce
pygame.init()


class QuantumCircut:
    levels = {1: [np.array([1, 0])], 2: [np.array([1,0]), np.array([0,1]),np.array([1,0])]}

    def __init__(self, level):
        self.level = level
        self.qubits = []
        self.box=[]
        for i in QuantumCircut.levels[level]:
            self.qubits.append(Qubit(i))
        self.states=[i.state for i in self.qubits]
        self.qSystem=reduce(np.kron,self.states)
        print(self.qSystem)

    def update(self, level):
        self.level = level
        self.qubits = []
        for i in QuantumCircut.levels[level]:
            self.qubits.append(Qubit(i))

    def display(self, surface, font):
        t = 550//(len(QuantumCircut.levels[self.level])+1)
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
