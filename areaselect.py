import pygame, pygame.freetype,sys
from helperFunctions import loadJson, arrayTo2D, createRectArray
from random import randrange
from game import Game
from levelselect import LevelSelect

class AreaSelect(object):
  def __init__(self):
    self.ELVETICA = pygame.freetype.Font('assets/Elvetica-Regular.otf',90)
    self.screen = pygame.display.get_surface()
    self.width, self.height = pygame.display.get_surface().get_size()
    self.running = True
    self.click = False

    self.colors = arrayTo2D(loadJson("levels/overview.json"),3,3)
    self.colors = self.greyOutColors(self.colors)
    self.boxDim = 120
    self.boxDist = 50
    self.rects = createRectArray(3,3,self.boxDist,self.boxDim)
    self.main()

  def main(self):
    while self.running:
      self.eventHandling()
      self.buttonHandling()
      self.draw()
  
  def eventHandling(self):
    self.click = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        self.click = True
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          self.running = False
  
  def buttonHandling(self):
    mx, my = pygame.mouse.get_pos()
    for x,row in enumerate(self.rects):
      for y,element in enumerate(row):
        if element.collidepoint((mx,my)):
          if self.click:
            LevelSelect(x*3+y)

  def draw(self):
    pygame.display.flip()
    self.screen.fill((255,255,230))
    self.ELVETICA.render_to(self.screen,(70,100),"Areas",(30,30,30))
    
    for x,row in enumerate(self.colors):
      for y,element in enumerate(row):
        pygame.draw.rect(self.screen,tuple(element['color']) , self.rects[x][y])

  def greyOutColors(self,array):
    for row in array:
      for element in row:
        if not element['solved']:
          element["color"] = [randrange(20,150)]*3
    return array

        

if __name__ == "__main__":
  pygame.init()
  pygame.font.init()
  width = 600
  height = 900

  screen = pygame.display.set_mode((width,height))
  AreaSelect()