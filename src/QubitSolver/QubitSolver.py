import pygame
from Qubit import Qubit
from Button import Button
from QuantumCircut import QuantumCircut
qCircut = QuantumCircut(2)
# (val, x, y, w, l, c1, c2)
buttons = [Button("X", 100, 630, 90, 80, (200, 200, 200), (20, 40, 20)),
           Button("H", 200, 630, 90, 80, (200, 200, 200), (20, 40, 20)),
           Button("CNOT", 300, 630, 90, 80, (200, 200, 200), (20, 40, 20)),
           Button("Measure", 10, 10, 130, 80, (200, 200, 200), (20, 40, 20))]

def modQubits():
 pass

def update():
 pass

def reDis():
 pass

pygame.init()
results=[]
compBasis=""
font = pygame.font.Font("Roboto-Black.ttf", 30)
screen = pygame.display.set_mode((960, 720))
clock = pygame.time.Clock()
running = True
compText = font.render("", True, (255, 255, 255))
screen.fill((0, 0, 0))
for i in buttons:
  i.display(screen, font, False)
while running:
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
         running = False
     if event.type == pygame.MOUSEBUTTONDOWN:
        for i in buttons:
           i.hover()
           i.display(screen, font, True)
           if i.over == True:
               if i.val == "Measure":
                  results.append(qCircut.compBasis())
                  compBasis = f"Measurements: {', '.join(results)}"
                  compText = font.render(compBasis, True, (255, 255, 255))
 for i in buttons:
     i.hover()
     i.display(screen, font, False)
 qCircut.display(screen,font)
 screen.blit(compText, (20, 570))
 pygame.display.flip()
 clock.tick(60)
pygame.quit()
