import pygame
from Qubit import Qubit
from Button import Button
from QuantumCircut import QuantumCircut

with open("save.txt","r") as save:  
  qCircut = QuantumCircut(int(save.read().strip()))
# (val, x, y, w, l, c1, c2)
buttons = [Button("How To Use", 30, 360, 130, 130, (10,10,10), (18, 3, 37)),
           Button("Start", 800, 360, 130, 130, (10,10,10), (18, 3, 37))]

pygame.init()
results=[]
hitB=[]
close=1
mode="s"
compBasis=""
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
screen.blit(startS)
for i in buttons:
  i.display(screen, font, False)

def reDis(isComp=False):
 screen.blit(backI) 
 for i in buttons:
  i.display(screen, font, False)
 qCircut.display(screen,font)
 if isComp:
    results=[]
    compBasis=""

def updateHit():
    hitB=[]
    # (val, x, y, w, l, c1, c2)
    print(qCircut.box)
    for i in range (len(qCircut.box)):               
        hitB.append(Button("hit",200,(qCircut.box[i][1])-30,750,60,(20,20,20),(230,230,230)))
    return(hitB)
while running:
 if mode=="s":
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      if event.type == pygame.MOUSEBUTTONDOWN:
          for i in buttons:
            i.hover()
            i.display(screen, font, True)
            if i.over == True:
                if i.val == "How To Use":
                    reDis(True)
                elif i.val == "Start":
                   buttons=[]
                   buttons = [Button("X", 100, 630, 90, 80, (10,10,10), (18, 3, 37)),
                              Button("H", 200, 630, 90, 80, (10,10,10), (18, 3, 37)),
                              Button("CNOT", 300, 630, 90, 80, (10,10,10), (18, 3, 37)),
                              Button("Measure", 10, 10, 130, 80, (10,10,10), (18, 3, 37)),
                              Button("New", 10, 100, 130, 80, (10,10,10), (18, 3, 37))]
                   mode="p"
                   reDis()
                   hitB=updateHit()
    for i in buttons:
      i.hover()
      i.display(screen, font, False)
 elif mode=="p":
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          if close>0:
            with open ("save.txt","w") as save:
                save.write(str(qCircut.level))
            close=close*-1
            mode="e"
          else:
            running = False
      if event.type == pygame.MOUSEBUTTONDOWN:
          for i in buttons:
            if i.over == True:
                if i.val == "Measure":
                    results.append(qCircut.compBasis())
                    compBasis = f"Measurements: {', '.join(results)}"
                    compText = font.render(compBasis, True, (255, 255, 255))
                    screen.blit(compText, (20, 570))
                elif i.val == "X":
                    reDis(True)
                elif i.val == "CNOT":
                    reDis(True)
                elif i.val == "H":
                    reDis(True)
                elif i.val == "New":
                    qCircut=QuantumCircut(1)
                    reDis(True)
                    hitB=updateHit()
                    print(hitB)

  for i in buttons:
      i.hover()
      i.display(screen, font, False)
  for i in hitB:
      i.hover()
 elif mode=="e":
     for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
     screen.blit(backI) 
     eText=sFont.render("Sucessfully saved, press the X again to quit the application.", True, (255, 255, 255))
     screen.blit(eText, (10, 300))


 pygame.display.flip()
 clock.tick(60)
pygame.quit()
