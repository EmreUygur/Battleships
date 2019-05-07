import os
import random
import numpy as np
from time import sleep

def select_difficulty():
  while 1:
    print(" Select Difficulty")
    print("     1) 4 ships, 4x4 map")
    print("     2) 6 ships, 6x6 map")
    print("     3) 8 ships, 8x8 map")
    difficulty = input(" Choose Difficulty (1-3): ")
    
    try:
      difficulty = int(difficulty)
      
      if(difficulty < 1 or difficulty >3):
        os.system("cls")
        print("#"*40,"BATTLESHIPS GAME","#"*40 )
        print()
        print(" Invalid Input !! Try Again...")
        
      else:
        os.system("cls")
        print("#"*40,"BATTLESHIPS GAME","#"*40 )
        print()
        return difficulty
        
    except:
      os.system("cls")
      print("#"*40,"BATTLESHIPS GAME","#"*40 )
      print()
      print(" Invalid Input !! Try Again...")

def cpu_map(numOfShips):
  map = np.zeros((numOfShips, numOfShips))
  
  for i in range(numOfShips):
    x = random.randint(0,numOfShips-1)
    y = random.randint(0,numOfShips-1)
    
    if(map[x][y] == 0):
      map[x][y] = 1
      break
      
  return map

