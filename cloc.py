import glob

def fileLength(file):
  with open(file) as f:
    for i, l in enumerate(f):
      pass
    return i+1
files = glob.glob("*.py")
length = 0
for file in files:
  length += fileLength(file)
print(length)
