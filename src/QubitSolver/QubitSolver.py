import pygame
from Qubit import Qubit
from Button import Button
from QuantumCircut import QuantumCircut
from QuantumGate import QuantumGate
import numpy as np

with open("save.txt", "r") as save:
    qCircut = QuantumCircut(int(save.read().strip()))
# (val, x, y, w, l, c1, c2)
buttons = [Button("How To Use", 30, 360, 130, 130, (10, 10, 10), (18, 3, 37)),
           Button("Start", 800, 360, 130, 130, (10, 10, 10), (18, 3, 37))]


pygame.init()
hitB = []
gates = {}
cGate = {"|0>": np.array([1, 0]), "|1>": np.array([0, 1])}
current = ""
close = 1
mode = "s"
compBasis = ""
font = pygame.font.Font("Roboto-Black.ttf", 20)
sFont = pygame.font.Font("Roboto-Black.ttf", 35)
screen = pygame.display.set_mode((960, 720))
startS = pygame.transform.smoothscale(pygame.image.load(
    'QubitSolverStart.png').convert_alpha(), (960, 720))
backI = pygame.transform.smoothscale(pygame.image.load(
    'QubitSolverBackground.png').convert_alpha(), (960, 720))
clock = pygame.time.Clock()
running = True
compText = font.render("", True, (255, 255, 255))
screen.blit(startS, (0, 0))
for i in buttons:
    i.display(screen, font, False)


def reDis(isComp=False):
   global compBasis
   screen.blit(backI, (0, 0))
   for i in buttons:
       i.display(screen, font, False)
   qCircut.display(screen, font)
   if isComp:
       compBasis = ""
   current = ""
   for i in gates:
       for i2 in gates[i]:
        pygame.draw.rect(screen, (45, 20, 65),
                         (i2[0], i2[1], 40, 40), 0, 10)
        gText = font.render(f"{i2[2]}", True, (230, 230, 230))
        screen.blit(gText, (i2[0]+13, i2[1]+7))


def selectCheck(val, index):
   global current
   if current == val:
       current = "none"
   else:
       current = buttons[index].val


def updateHit():
  hitB = []
  # (val, x, y, w, l, c1, c2)
  for i in range(len(qCircut.box)):
      hitB.append(Button(
          "hit", 200, (qCircut.box[i][1])-25, 750, 50, (20, 20, 20), (230, 230, 230)))
  return (hitB)


while running:
   if mode == "s":
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
           if event.type == pygame.MOUSEBUTTONDOWN:
               for i in buttons:
                   i.hover()
                   i.display(screen, font, True)
                   if i.over == True:
                       if i.val == "How To Use":
                           reDis()
                       elif i.val == "Start":
                           buttons = []
                           buttons = [Button("X", 140, 630, 90, 80,
                                              (10, 10, 10), (18, 3, 37)),
                                       Button("H", 240, 630, 90, 80,
                                              (10, 10, 10), (18, 3, 37)),
                                       Button("Y", 340, 630, 90, 80,
                                              (10, 10, 10), (18, 3, 37)),
                                       Button("Z", 440, 630, 90, 80,
                                              (10, 10, 10), (18, 3, 37)),
                                       Button("Measure", 10, 10, 130, 80,
                                              (10, 10, 10), (18, 3, 37)),
                                       Button("New", 10, 100, 130, 80,
                                              (10, 10, 10), (18, 3, 37)),
                                       Button("Delete", 10, 190, 130, 80,
                                              (10, 10, 10), (18, 3, 37)),
                                       Button("|0>", 30, 290, 90, 80,
                                              (10, 10, 10), (18, 3, 37)),
                                       Button("|1>", 30, 380, 90, 80,
                                              (10, 10, 10), (18, 3, 37)),]
                           mode = "p"
                           reDis()
                           hitB = updateHit()
       for i in buttons:
           i.hover()
           i.display(screen, font, False)
   elif mode == "p":
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               if close > 0:
                   with open("save.txt", "w") as save:
                       save.write(str(qCircut.level))
                   mode = "e"
           if event.type == pygame.MOUSEBUTTONDOWN:
               for i in range(len(buttons)):
                   if buttons[i].over:
                       if buttons[i].val == "Measure":
                           compBasis = qCircut.compBasis()
                           compText = font.render(
                               compBasis, True, (255, 255, 255))
                           bRect = compText.get_rect(center=(480, 590))
                           screen.blit(compText, bRect)
                       elif buttons[i].val in QuantumGate.gates:
                           reDis()
                           selectCheck(buttons[i].val, i)
                       elif buttons[i].val == "New":
                           gates = {}
                           qCircut = QuantumCircut(1)
                           reDis(True)
                           hitB = updateHit()
                       elif buttons[i].val == "Delete":
                           try:
                               del (gates[next(reversed(gates))][-1])
                               reDis()
                               if gates[next(reversed(gates))] == []:
                                   del (gates[next(reversed(gates))])
                           except:
                               print("No gates to delete")
                       elif "|" in buttons[i].val:
                        if np.array_equal(cGate[buttons[i].val], qCircut.qubits[0].state) and qCircut.level+1 in QuantumCircut.levels:
                           gates = {}
                           qCircut = QuantumCircut(qCircut.level+1)
                           reDis(True)
                           hitB = updateHit()
                        else:
                            mode = "f"
                            with open("save.txt", "w") as save:
                                save.write(str(1))
               for i in range(len(hitB)):
                   if hitB[i].over and current in QuantumGate.gates:
                        if hitB[i].toggle == False:
                            x, y = pygame.mouse.get_pos()
                        if i+1 in gates:
                            if gates[i+1][len(gates[i+1])-1][0] < x+40:
                                qCircut.addGate(current, i)
                                gates.setdefault(
                                    i+1, []).append((x-15, hitB[i].y+10, current))
                                pygame.draw.rect(screen,  (45, 20, 65),
                                                 (x-15, hitB[i].y+10, 40, 40), 0, 10)
                                gText = font.render(
                                    f"{current}", True, (230, 230, 230))
                                screen.blit(gText, (x-2, hitB[i].y+17))
                        else:
                            qCircut.addGate(current, i)
                            gates.setdefault(i+1, [(x-15, hitB[i].y+10, current)])
                            pygame.draw.rect(screen,  (45, 20, 65),
                                             (x-15, hitB[i].y+10, 40, 40), 0, 10)
                            gText = font.render(f"{current}", True, (230, 230, 230))
                            screen.blit(gText, (x-2, hitB[i].y+17))

       for i in buttons:
           i.hover()
           i.display(screen, font, False)
       for i in range(len(hitB)):
           if hitB[i].hover():
               x, y = pygame.mouse.get_pos()
               if current in QuantumGate.gates:
                   if i+1 in gates:
                        if gates[i+1][len(gates[i+1])-1][0] < x-40:
                            pygame.draw.rect(screen,  (45, 20, 65),
                                             (x-15, hitB[i].y+10, 40, 40), 0, 10)
                            gText = font.render(f"{current}", True, (230, 230, 230))
                            screen.blit(gText, (x-2, hitB[i].y+17))
                   else:
                       pygame.draw.rect(screen,  (45, 20, 65),
                                         (x-15, hitB[i].y+10, 40, 40), 0, 10)
                       gText = font.render(f"{current}",True,(230,230,230))
                       screen.blit(gText, (x-2,hitB[i].y+17))
           elif hitB[i].hover() ==False:
               reDis()
   elif mode == "e":
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
       screen.blit(backI, (0,0))
       eText = sFont.render(
           "Sucessfully saved, press the X again to quit the application.", True, (255, 255, 255))
       screen.blit(eText, (10, 300))
   elif mode =="f":
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
       screen.blit(backI, (0,0))
       eText = sFont.render(
           "You Have Finished All of the Levels", True, (255, 255, 255))
       screen.blit(eText, (200, 300))
   pygame.display.flip()
   clock.tick(60)
pygame.quit()
