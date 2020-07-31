###################################
# Module for all the methods to   #
# Generate a Level                #
###################################

import random
from random import randrange
import operator
from scramble import *

def genMenuMatrix(width,height):
  c = genRandomColors()
  return genColorMatrix(c[0],c[1],c[2],c[0],width,height)


def genLevel(col,dim,scramble):
  matrixList = genColorMatrix(col[0],col[1],col[2],col[3],dim[0],dim[1])
  matrixDic = colMatrixToDicMatrix(matrixList)

  if scramble == "lane":
    matrix = scrambleMatrixLane(matrixDic)
  if scramble == "frame":
    matrix = scrambleMatrixFrame(matrixDic)
  if scramble == "corners":
    matrix = scrambleMatrixCorners(matrixDic)
  if scramble == "barsInner":
    matrix = scrambleMatrixPrisonBarsInner(matrixDic)
  if scramble == "barsOuter":
    matrix = scrambleMatrixPrisonBarsOuter(matrixDic)
  if scramble == "checkerboard":
    matrix = scrambleMatrixCheckerboard(matrixDic)
  return matrix

def genRandomLevel(width,height):
  # Generate RandomColors
  c = genRandomColors()
  # Get the Gradient
  matrixList = genColorMatrix(c[0],c[1],c[2],c[3],width,height)
  # Format with Game Data
  matrixDic = colMatrixToDicMatrix(matrixList)    
  # Return the Randomized List
  return scrambleMatrixFrame(matrixDic)

def genRandomColors():
  colors = []
  for _ in range(4):
    colors.append((randrange(0,255),randrange(0,255),randrange(0,255)))
  return colors

def colMatrixToDicMatrix(colMatrix):
    matrix = []
    for x in range(len(colMatrix)):
      matrix.append([])
      for y in range(len(colMatrix[0])):
        matrix[x].append({"rgb": colMatrix[x][y], "clicked": False, "origPos": (x,y),"draggable": False})
    return matrix

def genColorMatrix(linksOben, rechtsOben, linksUnten, rechtsUnten, width, height):
  oben = interpolateColors(linksOben,rechtsOben,width)
  rechts = interpolateColors(rechtsOben,rechtsUnten,height)
  unten= interpolateColors(linksUnten,rechtsUnten,width)
  links= interpolateColors(linksOben,linksUnten,height)

  firstImage = []
  for x in range(width):
    for y in range(height):
      firstImage.append(interpolateColors(links[y],rechts[y],width))
  firstImage = list(zip(*firstImage[::-1]))

  secondImage = []
  for y in range(height):
    for x in range(width):
      secondImage.append(interpolateColors(oben[x],unten[x],height))
  secondImage = list(map(lambda x: list(x[::-1]),secondImage))

  finalImage = []
  for x in range(width):
    tempList = []
    for y in range(height):
      t = tuple(map(operator.add,firstImage[x][y],secondImage[x][y]))
      t = tuple(map(operator.truediv, t,(2,2,2)))
      t = tuple(map(int,t))
      tempList.append(t)
    finalImage.append(tempList)
  return finalImage


def interpolateColors(c1, c2, length):
  colorRange = []
  redStep = (c2[0] - c1[0]) / length
  greenStep = (c2[1] - c1[1]) / length
  blueStep = (c2[2] - c1[2]) / length

  colorRange.append(c1)
  for i in range(length-1):
    colorRange.append(tuple(map(operator.add, colorRange[i],(redStep,greenStep,blueStep))))
  return list(map(lambda x: tuple(map(int,x)),colorRange))
