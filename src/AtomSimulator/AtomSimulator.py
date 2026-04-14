import pygame
from Atom import Atom
from Button import Button
from Electron import Electron
from Molecule import Molecule
atoms=[Atom(500,300)]
buttons=[]
def modAtoms():
   pass
def update():
   pass
def reDis():
   pass
pygame.init()
screen = pygame.display.set_mode((960, 720))
clock = pygame.time.Clock()
running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
   screen.fill((0,0,0))
   gen=atoms[0].move()
   off=0
   i=0
   for aData in gen:
       if atoms[0].nucleus.protons+atoms[0].nucleus.neutrons<i:
          pygame.draw.circle(screen, aData[0],(aData[1][0]+atoms[0].Nucleus.r*2,aData[1][0]),aData[2])
       else:
          pygame.draw.circle(screen, aData[0],aData[1],aData[2])
   pygame.display.flip()
   clock.tick(60)
pygame.quit()
