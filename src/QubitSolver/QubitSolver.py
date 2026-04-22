import pygame
from Qubit import Qubit
from Button import Button
from QuantumCircut import QuantumCircut


with open("save.txt","r") as save: 
 qCircut = QuantumCircut(int(save.read().strip()))
# (val, x, y, w, l, c1, c2)
buttons = [Button("How To Use", 420, 360, 130, 80, (200, 200, 200), (20, 40, 20)),
          Button("Start", 420, 270, 130, 80, (200, 200, 200), (20, 40, 20))]


def modQubits():
pass


def update():
pass


def reDis(isComp=False):
screen.fill((0, 0, 0))
for i in buttons:
 i.display(screen, font, False)
qCircut.display(screen,font)
if isComp:
   results=[]
   compBasis=""


pygame.init()
results=[]
mode="s"
compBasis=""
font = pygame.font.Font("Roboto-Black.ttf", 20)
sFont = pygame.font.Font("Roboto-Black.ttf", 50)


screen = pygame.display.set_mode((960, 720))
clock = pygame.time.Clock()
running = True
compText = font.render("", True, (255, 255, 255))
screen.fill((0, 0, 0))
for i in buttons:
 i.display(screen, font, False)


sText=sFont.render("Qubit Solver", True, (255, 255, 255))
screen.blit(sText, (350, 50))


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
                  buttons = [Button("X", 100, 630, 90, 80, (200, 200, 200), (20, 40, 20)),
                             Button("H", 200, 630, 90, 80, (200, 200, 200), (20, 40, 20)),
                             Button("CNOT", 300, 630, 90, 80, (200, 200, 200), (20, 40, 20)),
                             Button("Measure", 10, 10, 130, 80, (200, 200, 200), (20, 40, 20)),
                             Button("How To Use", 10, 100, 130, 80, (200, 200, 200), (20, 40, 20)),
                             Button("New", 10, 190, 130, 80, (200, 200, 200), (20, 40, 20))]
                  mode="p"
                  reDis()
   for i in buttons:
     i.hover()
     i.display(screen, font, False)
elif mode=="p":
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
         with open ("save.txt","w") as save:
           save.write(qCircut.level)
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


 for i in buttons:
     i.hover()
     i.display(screen, font, False)
pygame.display.flip()
clock.tick(60)
pygame.quit()
