import pygame,pygame.freetype, sys
from levelSetup import genRandomLevel, genMenuMatrix, genLevel
from helperFunctions import draw_circle, checkSorted, darkenColor
from areaselect import AreaSelect

pygame.init()
pygame.font.init()

ELVETICA = pygame.freetype.Font('assets/Elvetica-Regular.otf',50)

width = 600
height = 900

screen = pygame.display.set_mode((width,height))

pygame.display.set_caption("Hue")
icon = pygame.image.load("assets/icon.png").convert_alpha()
pygame.display.set_icon(icon)

class MainMenu(object):
  def __init__(self):
    self.width, self.height = pygame.display.get_surface().get_size()
    self.buttonStart = pygame.Rect(300,800,300,100)
    self.click = False
    self.colorMatrix = self.matrix()
    self.boxWidth = int(width/len(self.colorMatrix))
    self.boxHeight = int(height/len(self.colorMatrix[0])*0.6)

    self.main()
  
  def matrix(self):
    matrix = genMenuMatrix(6,5)
    temp = matrix[1][1]
    matrix[1][1] = matrix[4][3]
    matrix[4][3] = temp
    return matrix

  def main(self):
    running = True
    while running:
      self.eventHandling()
      self.buttonHandling() 
      self.draw()

  def eventHandling(self):
    self.click = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False
          pygame.quit()
          sys.exit()
        if event.key == pygame.K_r:
          self.colorMatrix = self.matrix()
      
      if event.type == pygame.MOUSEBUTTONDOWN:
        self.click = True

  def buttonHandling(self):
    mx, my = pygame.mouse.get_pos()
    if self.buttonStart.collidepoint((mx,my)):
      if self.click:
        pygame.time.delay(100)
        AreaSelect()

  def draw(self):
    screen.fill((255,255,230))
    for x,row in enumerate(self.colorMatrix):
      for y,element in enumerate(row):
        boxPosX = self.boxWidth * x
        boxPosY = self.boxHeight * y
        pygame.draw.rect(screen, element, pygame.Rect(boxPosX,boxPosY,self.boxWidth,self.boxHeight))

    ELVETICA.render_to(screen,(320,820),"Start Game",(30,30,30))
    pygame.display.update()

if __name__ == "__main__":
  MainMenu()