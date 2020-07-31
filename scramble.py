###########################
# Module with functions   #
# to scramble the matrix  #
# and fix cells in place  # 
# in certain patterns     #
########################### 
import random

def scrambleMatrixLane(matrix):
  copy = matrix[1:len(matrix)-1]
  random.shuffle(copy)
  for row in copy:
    random.shuffle(row)
    for element in row:
      element["draggable"] = True
  matrix[1:len(matrix)-1] = copy
  return matrix

def scrambleMatrixFrame(matrix):
  temp = matrix[1:len(matrix)-1]
  copy = []
  for row in temp:
    copy.append(row[1:len(row)-1])

  random.shuffle(copy)
  for row in copy:
    random.shuffle(row)
    for element in row:
      element["draggable"] = True
  
  for x,row in enumerate(temp):
    row[1:len(row)-1] = copy[x]
  matrix[1:-1] = temp
  return matrix

def scrambleMatrixCorners(matrix):
  copy = []
  copy.append(matrix[0][1:len(matrix[0])-1])
  for x in range(1,len(matrix)-1):
    copy.append(matrix[x])
  copy.append(matrix[-1][1:len(matrix[0])-1])


  subcopy = copy[1:-1]
  random.shuffle(subcopy)
  copy[1:len(copy)-1] = subcopy

  tmp = copy[0]
  copy[0] = copy[-1]
  copy[-1] = tmp 

  for row in copy:
    random.shuffle(row)
    for element in row:
      element["draggable"] = True

  copy[0].insert(0,matrix[0][0])
  copy[0].append(matrix[0][len(matrix[0])-1])

  copy[len(copy)-1].insert(0,matrix[len(copy)-1][0])
  copy[len(copy)-1].append(matrix[len(copy)-1][len(matrix[0])-1])
  return copy

def scrambleMatrixPrisonBarsInner(matrix):
  copy=[]
  for x, row in enumerate(matrix):
    if x % 2 == 0:
      copy.append(row)

  random.shuffle(copy)
  for row in copy:
    random.shuffle(row)
    for element in row:
      element["draggable"] = True
  
  for x, row in enumerate(matrix):
    if x % 2 == 0:
      matrix[x] = copy[round(x/2)]
  return matrix

def scrambleMatrixPrisonBarsOuter(matrix):
  copy=[]
  for x, row in enumerate(matrix):
    if x % 2 != 0:
      copy.append(row)
  
  random.shuffle(copy)
  for row in copy:
    random.shuffle(row)
    for element in row:
      element["draggable"] = True
  
  for x, row in enumerate(matrix):
    if x % 2 != 0:
      matrix[x] = copy[int(x/2)]
  return matrix
  
def scrambleMatrixCheckerboard(matrix):
  copy = []
  
  for x, row in enumerate(matrix):
    for y , element in enumerate(row):
      if (x*len(matrix[0])+y) % 2 == 1:
        copy.append(element)

  random.shuffle(copy)
  for element in copy:
    element["draggable"] = True

  counter = 0
  for x, row in enumerate(matrix):
    for y, element in enumerate(row):
      if (x*len(matrix[0])+y) % 2 ==1:
        matrix[x][y] = copy[counter]
        counter +=1
  return matrix