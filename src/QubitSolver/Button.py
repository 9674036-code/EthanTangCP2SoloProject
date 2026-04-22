import pygame
pygame.init()




class Button:
def __init__(self, val, x, y, w, l, c1, c2, toggle=1):
    self.val = val
    self.x = x
    self.y = y
    self.w = w
    self.l = l
    self.c1 = c1
    self.c2 = c2
    self.over = False
    self.toggle=toggle


def display(self, screen, font, mouseClicked):
      if self.over == False:
          pygame.draw.rect(screen, self.c1, [
                          self.x, self.y, self.w, self.l], 0, 30)
      elif self.over == True and mouseClicked == False:
          pygame.draw.rect(screen, self.c2, [
                          self.x, self.y, self.w, self.l], 0, 30)


      text = font.render(self.val, True, (255, 255, 255))
      textRect = text.get_rect()
      textRect.center = (self.x + self.w/2, self.y + self.l/2)
      screen.blit(text, textRect)
def hover(self):
      mouseX, mouseY = pygame.mouse.get_pos()
      if mouseX <= self.x + self.w and mouseX >= self.x and mouseY >= self.y and mouseY <= self.y + self.l:
          self.over = True
      else:
          self.over = False
