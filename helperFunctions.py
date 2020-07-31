###################
# Helper Functions#
###################

from pygame import gfxdraw
import pygame
import json

def checkSorted(matrix, width, height):
  isSorted = True
  for x in range(width):
    for y in range(height):
      if not matrix[x][y]["origPos"] == (x,y):
        isSorted = False
  return isSorted

def draw_circle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)

def darkenColor(color):
  return tuple(map(lambda x: round(x/2),color))


def loadJson(path):
  with open(path) as json_file:
    data = json.load(json_file)
  return data

def saveJson(path, data):
  with open(path,'w') as outfile:
    json.dump(data,outfile)

def arrayTo2D(array,width,height):
  twoDArray = []
  for i in range(height):
    twoDArray.append(array[i*width:(i+1)*width])
  return twoDArray

def createRectArray(width,height,boxDist,boxDim):
  array = []
  for y in range(height):
    row = []
    for x in range(width):
      boxPosX = (boxDist+boxDim)*x+70
      boxPosY = (boxDist+boxDim)*y+250
      row.append(pygame.Rect(boxPosX,boxPosY,boxDim,boxDim))
    array.append(row)
  return array

def setLevelSolved(area,level):
  path = "levels/" + str(area) + ".json"
  areaData = loadJson(path)
  areaData["levels"][level]["solved"] = True
  saveJson(path, areaData)


def checkAreaSolved(area):
 path = "levels/" +str(area) + ".json"
 areaData = loadJson(path) 
 solved = True
 for level in areaData["levels"]:
   if not level["solved"]:
     soved = False
 if solved:
   areas = loadJson("levels/overview.json")
   areas[area]["solved"] = True
   saveJson("levels/overview.json",areas)