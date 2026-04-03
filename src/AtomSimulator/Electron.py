class Electron:
   def __init__(self,x,y):
       self.r=3
       self.angle=0
       self.spin=1
       self.reX=x
       self.reY=y
   def display(self):
       return ((241,194,50),(self.reX,self.reY),self.r)
