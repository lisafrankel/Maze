# maze program by Lisa Frankel


# tests follow here

doTests = 1
if doTests:
  # Test #1
  m = Maze()
  if m.__class__ == Maze:
    printNow("Test 1 passed, Maze exists.")
  else:
    printNow("Test 1 failed, Maze does not exist")