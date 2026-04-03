class Nucleus:
   def __init__(self,x,y,protons,neutrons):
       self.r=10
       self.x=x
       self.y=y
       self.protons=protons
       self.neutrons=neutrons
       self.color=(204,0,0)
   def changeC(self):
       if self.color==(204,0,0):
           self.color=(243,243,243)
       else:
           self.color=(204,0,0)
   def display(self):
       return (self.color,(self.y,self.y),self.r)
