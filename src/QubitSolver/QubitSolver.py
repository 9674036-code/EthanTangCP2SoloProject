import pygame
from Qubit import Qubit
from Button import Button
from QuantumCircut import QuantumCircut
from QuantumGate import QuantumGate


with open("save.txt", "r") as save:
    qCircut = QuantumCircut(int(save.read().strip()))
# (val, x, y, w, l, c1, c2)
buttons = [Button("How To Use", 30, 360, 130, 130, (10, 10, 10), (18, 3, 37)),
          Button("Start", 800, 360, 130, 130, (10, 10, 10), (18, 3, 37))]


pygame.init()
results = []
hitB = []
gates = []
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
   for i in gates:
       pygame.draw.rect(screen, (230,230,230),(i[0],i[1],30,30),0,10)

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
                           buttons = [ Button("X", 100, 630, 90, 80,
                                               (10, 10, 10), (18, 3, 37)),
                                       Button("H", 200, 630, 90, 80,
                                               (10, 10, 10), (18, 3, 37)),
                                       Button("CNOT", 300, 630, 90, 80,
                                               (10, 10, 10), (18, 3, 37)),
                                       Button("Measure", 10, 10, 130, 80,
                                               (10, 10, 10), (18, 3, 37)),
                                       Button("New", 10, 100, 130, 80,
                                               (10, 10, 10), (18, 3, 37)),
                                       Button("Delete", 10, 190, 130, 80,
                                             (10, 10, 10), (18, 3, 37)),
                                       Button("|0>", 300, 790, 90, 80,
                                             (10, 10, 10), (18, 3, 37)),
                                       Button("|1>", 300, 700, 90, 80,
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
                           print(hitB)
                       elif buttons[i].val == "Delete":
                           try:
                               del gates[len(gates)-1]
                               reDis()
                           except:
                               print("No gates to delete")
               for i in range(len(hitB)):
                   if hitB[i].over and current in QuantumGate.gates:
                       qCircut.addGate(current, i)
                       gates.append((((hitB[i].w/2)+hitB[i].x)-15,hitB[i].y+15))
                       if i not in qCircut.gates:
                           pygame.draw.rect(screen, (230, 230, 230),
                            (((hitB[i].w/2)+hitB[i].x)-15, hitB[i].y+15, 30, 30), 0, 10)
                       else:
                            pygame.draw.rect(screen, (230, 230, 230),
                             (((hitB[i].w/(len(qCircut.gates[i])+1))+hitB[i].x)-15, hitB[i].y+15, 30, 30), 0, 10)


       for i in buttons:
           i.hover()
           i.display(screen, font, False)
       for i in hitB:
           if i.hover():
               if current in QuantumGate.gates:
                   pygame.draw.rect(screen, (230, 230, 230),
                                   (((i.w/2)+i.x)-15, i.y+15, 30, 30), 0, 10)
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
   pygame.display.flip()
   clock.tick(60)
pygame.quit()
