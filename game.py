import pygame, sys
from levelSetup import genRandomLevel, genLevel
from helperFunctions import draw_circle, checkSorted, darkenColor, setLevelSolved,checkAreaSolved



class Game(object):
  def __init__(self,area=None,level=None,levelData = None):
    self.screen = pygame.display.get_surface()
    self.width , self.height = pygame.display.get_surface().get_size()

    if levelData:
      self.colorMatrix = genLevel(levelData['color'],levelData['dimensions'],levelData['scrambled'])
      self.matwidth = levelData['dimensions'][0]
      self.matheight = levelData['dimensions'][1]
    else:
      self.matwidth = 5
      self.matheight = 5
      self.colorMatrix = genRandomLevel(self.matwidth,self.matheight)

    self.boxWidth = round(self.width/self.matwidth)
    self.boxHeight = round(self.height/self.matheight)

    self.area = area
    self.level = level
    
    self.clickedX = -1
    self.clickedY = 0

    self.mouseOffsetX = 0
    self.mouseOffsetY = 0

    self.alpha = 0
    self.solved = False
    self.main()

  def main(self, levelData = None):
    running = True
    while running:
      mx,my = pygame.mouse.get_pos()

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          pygame.quit()
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.solved:
            running = False
          else:
            if event.button == 1:
              x = int(mx/self.boxWidth)
              y = int(my/self.boxHeight)
              if self.colorMatrix[x][y]["draggable"]:
                self.clickedX = x
                self.clickedY = y
                self.mouseOffsetX = mx % self.boxWidth
                self.mouseOffsetY = my % self.boxHeight
                self.colorMatrix[x][y]["clicked"] = True
            
        if event.type == pygame.MOUSEBUTTONUP:
          if event.button == 1:
            self.colorMatrix[self.clickedX][self.clickedY]["clicked"] = False
            x = int(mx/self.boxWidth)
            y = int(my/self.boxHeight)
            if self.colorMatrix[x][y]["draggable"] and self.clickedX >= 0:
              temp = self.colorMatrix[x][y]
              self.colorMatrix[x][y] = self.colorMatrix[self.clickedX][self.clickedY]
              self.colorMatrix[self.clickedX][self.clickedY] = temp
              if checkSorted(self.colorMatrix,self.matwidth,self.matheight):
                self.solved = True
                setLevelSolved(self.area,self.level)
                checkAreaSolved(self.area)
                print('solved')
                self.alpha = 175

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_r:
            self.colorMatrix = genRandomLevel(self.matwidth,self.matheight)
          if event.key == pygame.K_ESCAPE:
            running = False

      self.draw(mx,my)

  def draw(self,mx,my):
    pygame.display.flip()
    self.screen.fill((255,255,230))

    radius = round(self.boxWidth/20)
    draggedCell = None
    for x,row in enumerate(self.colorMatrix):
      for y,element in enumerate(row):
        boxPosX = self.boxWidth * x
        boxPosY = self.boxHeight * y
        if not element["clicked"]:
          pygame.draw.rect(self.screen, element["rgb"], pygame.Rect(boxPosX,boxPosY,self.boxWidth,self.boxHeight))
        else:
          draggedCell = element
        if not element["draggable"]:
          circlePosX = boxPosX + round(self.boxWidth/2)
          circlePosY = boxPosY + round(self.boxHeight/2)
          draw_circle(self.screen,circlePosX,circlePosY,radius,darkenColor(element["rgb"]))
    if draggedCell:
      posX = mx-self.mouseOffsetX
      posY = my-self.mouseOffsetY
      pygame.draw.rect(self.screen,draggedCell["rgb"],pygame.Rect(posX,posY,self.boxWidth,self.boxHeight))

    if self.alpha > 0:
      s = pygame.Surface((self.width,self.height))
      s.set_alpha(self.alpha)
      s.fill((255,255,255))
      self.screen.blit(s,(0,0))
      if self.alpha > 5:
        self.alpha = self.alpha *0.992
      else:
        self.alpha -= 0.5