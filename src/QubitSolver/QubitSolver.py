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
results = []
hitB = []
gates = {}
cGate={"|0>":np.array([1, 0]),"|1>":np.array([0, 1])}
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
screen.blit(startS,(0,0))
for i in buttons:
    i.display(screen, font, False)


def reDis(isComp=False):
   global results
   global compBasis
   screen.blit(backI,(0,0))
   for i in buttons:
       i.display(screen, font, False)
   qCircut.display(screen, font)
   if isComp:
       results = []
       compBasis = ""
   print(gates)
   current=""
   for i in gates:
       for i2 in gates[i]:
        pygame.draw.rect(screen, (230,230,230),(i2[0],i2[1],30,30),0,10)

def selectCheck(val, index):
   global current
   if current == val:
       current = "none"
   else:
       current = buttons[index].val
   print(current)

def updateHit():
  hitB = []
  # (val, x, y, w, l, c1, c2)
  print(qCircut.box)
  for i in range(len(qCircut.box)):
      hitB.append(Button(
          "hit", 200, (qCircut.box[i][1])-30, 750, 60, (20, 20, 20), (230, 230, 230)))
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
                           buttons = [ Button("X", 140, 630, 90, 80,
                                               (10, 10, 10), (18, 3, 37)),
                                       Button("H", 240, 630, 90, 80,
                                               (10, 10, 10), (18, 3, 37)),
                                       Button("CNOT", 340, 630, 90, 80,
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
                           results.append(qCircut.compBasis())
                           compBasis = f"Measurements: {', '.join(results)}"
                           compText = font.render(compBasis, True, (255, 255, 255))
                           print(compText)
                       elif buttons[i].val in QuantumGate.gates:
                           reDis()
                           selectCheck(buttons[i].val, i)
                       elif buttons[i].val == "New":
                           qCircut = QuantumCircut(1)
                           reDis(True)
                           hitB = updateHit()
                           gates=[]
                       elif buttons[i].val == "Delete":
                           try:
                               del gates[len(gates)-1]
                               reDis()
                           except:
                               print("No gates to delete")
                       elif "|" in buttons[i].val:
                        if np.array_equal(cGate[buttons[i].val],qCircut.qubits[0].state) and qCircut.level+1 in QuantumCircut.levels:
                           qCircut = QuantumCircut(qCircut.level+1)
                           reDis(True)
                           hitB = updateHit()
                           gates=[]
                        else:
                            mode="f"
               for i in range(len(hitB)):
                    if hitB[i].over and current in QuantumGate.gates:
                        if hitB[i].toggle==False:
                            x,y=pygame.mouse.get_pos()
                        try:
                            if gates[i+1][len(gates)-1][0]<x+40:
                                qCircut.addGate(current, i)
                                gates.setdefault(i+1,[(x,hitB[i].y+15)])
                                pygame.draw.rect(screen, (230, 230, 230),
                                    (x, hitB[i].y+15, 30, 30), 0, 10)
                        except:
                            qCircut.addGate(current, i)
                            gates.setdefault(i+1,[(x,hitB[i].y+15)])
                            pygame.draw.rect(screen, (230, 230, 230),
                                    (x, hitB[i].y+15, 30, 30), 0, 10)

       for i in buttons:
           i.hover()
           i.display(screen, font, False)
       for i in hitB:
           if i.hover():
               if current in QuantumGate.gates:
                   x,y=pygame.mouse.get_pos()
                   pygame.draw.rect(screen, (230, 230, 230),
                                   (x, i.y+15, 30, 30), 0, 10)
                   print(True)
           elif i.hover()==False:
               reDis()
   elif mode == "e":
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
       screen.blit(backI,(0,0))
       eText = sFont.render(
           "Sucessfully saved, press the X again to quit the application.", True, (255, 255, 255))
       screen.blit(eText, (10, 300))
   elif mode=="f":
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
       screen.blit(backI,(0,0))
       eText = sFont.render(
           "You Have Finished All of the Levels", True, (255, 255, 255))
       screen.blit(eText, (200, 300))
   pygame.display.flip()
   clock.tick(60)
pygame.quit()
