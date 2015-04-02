# maze program by Lisa Frankel

setMediaPath('/Users/Lisa/Desktop/College/4 Spring Term 2015/Computer Science 1 - Multimedia/Maze/')

class Maze(object):
  """ solves a maze """

  def __init__(self):
    """Initialization"""
    self.image = makePicture("maze.jpg")

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

