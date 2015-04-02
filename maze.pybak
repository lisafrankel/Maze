# maze program by Lisa Frankel

setMediaPath('/Users/Lisa/Desktop/College/4 Spring Term 2015/Computer Science 1 - Multimedia/Maze/')

class Maze(object):
  """ solves a maze """

  def __init__(self):
    """Initialization"""
    self.image = makePicture("maze.jpg")
    self.w = makeWorld(getWidth(self.image), getHeight(self.image))
    self.w.setPicture(self.image)

# tests follow here

doTests = 1
if doTests:
  # Test 1
  m = Maze()
  if m.__class__ == Maze:
    printNow("Test 1 passed, Maze exists.")
  else:
    printNow("Test 1 failed, Maze does not exist.")
    
  # Test 2
  if m.image.__class__ == Picture:
    printNow("Test 2 passed, Image exists.")
  else:
    printNow("Test 2 failed, Image doesn't exist.")
  
  # Test 3
  try:
    if m.w.__class__ == World:
      printNow("Test 3 passed, World exists.")
  except:
    printNow("Test 3 failed, World doesn't exist.")
  
  # Test 4
  try:
    if m.w.getPicture().fileName[-8:] == 'maze.jpg':
      printNow("Test 4 passed, World Picture is maze.jpg.")
    else:
      printNow("Test 4 failed, World Picture is not maze.jpg" + m.w.getPicture().fileName)
  except:
    printNow("Test 4 failed, unable to get file name")