import pygame, pygame.freetype,sys
from helperFunctions import loadJson, arrayTo2D, createRectArray
from levelSetup import genColorMatrix
from random import randrange
from game import Game

class LevelSelect(object):
  def __init__(self, number):
    self.ELVETICA = pygame.freetype.Font('assets/Elvetica-Regular.otf',90)
    self.screen = pygame.display.get_surface()
    self.width, self.hieght = pygame.display.get_surface().get_size()
    self.running = True
    self.click = False

    self.number = number

    self.jsonData = loadJson("levels/" + str(number) + ".json")
    self.levels = self.jsonData['levels']
    col = self.jsonData['color']
    self.colors = genColorMatrix(col[0],col[1],col[2],col[3],6,6)
    self.colors = self.greyOutColors(self.colors)
    self.boxDim = 60
    self.boxDist = 18
    self.rects = createRectArray(6,6,self.boxDist,self.boxDim)
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
    mx,my = pygame.mouse.get_pos()
    for x,row in enumerate(self.rects):
      for y,element in enumerate(row):
        if element.collidepoint((mx,my)):
          if self.click:
            Game(self.number,x*6+y,self.levels[x*6+y])

  def draw(self):
    pygame.display.flip()
    self.screen.fill((255,255,230))
    self.ELVETICA.render_to(self.screen,(70,100),"Levels",(30,30,30))  

    for x, row in enumerate(self.colors):
      for y, element in enumerate(row):
        pygame.draw.rect(self.screen,tuple(element),self.rects[x][y])

  def greyOutColors(self,array):
    for x,row in enumerate(array):
      for y,element in enumerate(row):
        if not self.levels[x*len(array)+y]["solved"]:
          array[x][y] = (randrange(20,150),)*3
    return array