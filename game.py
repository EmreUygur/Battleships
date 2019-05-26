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

def user_map(numOfShips):
  
  map = np.zeros((numOfShips,numOfShips))
  
  for i in range(numOfShips):
    (x,y) = addShip(numOfShips, map)
    map[x][y] = 1
    
  return map

def addShip(numOfShips, map):
  while 1:
    x = input("X coordinate:")
    y = input("Y coordinate:")
    
    try:
      x = int(x)
      y = int(y)
      if((x<0 or x>=numOfShip) or (y<0 or y>=numOfShip)):
        os.system("cls")
        print("Out of Range")
        
      else:
        if(array[x][y] == 0):
          os.system("cls")
          return(x,y)
        else:
          os.system("cls")
          print("X:",x,"Y:",y," Coordinate is not empty. Find another coordinate")
    except:
      os.system("cls")
      print("Invalid Characters")
      
def map(pc_map, user_map, difficulty):
  os.system("cls")
  print("#"*40,"AMIRAL BATTI","#"*40)
  print("")
  print("")


  x = 2*(difficulty+1)
  y = x

  pc_score = 0
  player_score = 0


  print("OYUNCU", end="")
  print(" "*10, end="")
  print(" "*(20+8*(difficulty-1)), end="BILGISAYAR \n")

  print("", end="   ")
  for i in range(x):
      print(i, end="   ")

  print("                 ",end="   ")
  for i in range(x):
      print(i, end="   ")

  for i in range(y):

      print("")
      print("")
      for j in range(x):

          if(j == 0):
              print(i, end="  ")

          if(player_map[j][i] == 0):
              print("~", end="   ")

          elif(player_map[j][i] == 1):
              print("#", end="   ")
          elif(player_map[j][i] == 2):
              print("X", end="   ")
              pc_score += 1
          elif(player_map[j][i] == 3):
              print("O", end="   ")
      print("                 ",end="")

      for j in range(x):

          if(j == 0):
              print(i, end="  ")

          if(pc_map[j][i] == 2):
              print("X", end="   ")
              player_score += 1
          elif(pc_map[j][i] == 3):
              print("O", end="   ")
          else:
              print("~", end="   ")

  print("\n")
  print("GAME DIFFICULTY                           : ", difficulty)
  print("# OF SHIPS USER SUNK                      : ", player_score)
  print("# OF SHIPS USER LOST GEMILERINIZIN SAYISI : ", pc_score)
  print("# OF SHIPS OF USER'S LEFT                 : ", (x- pc_score))

  if((x - pc_score) == 0):
      # OYUNCU KAYBEDER
      return 0
  elif((x - player_score) == 0):
      # OYUNCU KAZANIR
      return 1
  else:
      # OYUNA DEVAM
      return 2

 
