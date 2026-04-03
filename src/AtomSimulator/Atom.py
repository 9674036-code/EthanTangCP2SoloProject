from Electron import Electron
from Nucleus import Nucleus


class Atom:
   def __init__(self,x,y):
       self.x=x
       self.y=y
       self.nucleus=Nucleus(x,y,1,1)
       self.electrons=[]
       self.electrons.append(Electron(x,y))


   def Zeff(self):
       pass
   def move(self):
       for i in range(self.nucleus.protons):
           yield self.nucleus.display()
       self.nucleus.changeC()
       for i in range(self.nucleus.neutrons):
           yield self.nucleus.display()
       for i in range(len(self.electrons)):
           yield self.electrons[i].display()
