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
  print("#"*40,"BATTLESHIPS GAME","#"*40)
  print("")
  print("")


  x = 2*(difficulty+1)
  y = x

  pc_score = 0
  player_score = 0


  print("PLAYER", end="")
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
  print("# OF SHIPS USER LOST                      : ", pc_score)
  print("# OF SHIPS OF USER'S LEFT                 : ", (x- pc_score))

  if((x - pc_score) == 0):
      # PLAYER LOST
      return 0
  elif((x - player_score) == 0):
      # PLAYER WIN
      return 1
  else:
      # CONTINUE TO GAME
      return 2

def game(pc_map, user_map, difficulty, numOfShips):
  counter = 0
  
  while 1:
    os.system("cls")
    print("#"*40,"BATTLESHIPS GAME","#"*40)
    result = map(pc_map, user_map, difficulty)
    
    if(result == 0):
      print("!!! YOU LOST !!!")
      break
    elif(result == 1):
      print("!!! YOU WIN !!!")
      break
      
    if(counter%2 == 0):
      #USER'S TURN
      shoot("USER", user_map, numOfShips)
    else:
      #CPU'S TURN
      shoot("CPU", pc_map, numOfShips)
    
    counter += 1
    
def shoot(shooter, map, numOfShips):
  if(shooter == "USER"):
    while 1:
      x = input("X coordinate:")
      y = input("Y coordinate:")
      
      try:
        x = int(x)
        y = int(y)
        if((x<0 or x>=numOfShips) or (y<0 or y>=numOfShips)):
          print("Out of Map. Please Choose Proper Coordinates")
            else:
              if(map[x][y] == 0):
                #print("MISS")
                map[x][y] = 3
                break
              elif(map[x][y] == 1):
                #print("HIT")
                map[x][y] = 2
                break
              elif(map[x][y] == 2 or map[x][y] == 3):
                print("X:",x,"Y:",y," Coordinate Was Hit Before. Please Choose Another Coordinate")
                  else:
                    print("Unexpected Error. Please Choose Different Coordinate")
      except:
                print("Invalid Character(s)")
  else:
    while 1:
    x = random.randint(0,numOfShips-1)
    y = random.randint(0,numOfShips-1)
    if(map[x][y] == 0):
      #print("MISS")
      map[x][y] = 3
      break
    elif(map[x][y] == 1):
      #print("HIT")
      map[x][y] = 2
     break

  return map

def main_menu():
  os.system("cls")
  print("#"*40,"BATTLESHIPS GAME","#"*40)
  print()
  difficulty = select_difficulty()
  numOfShips = 2*(difficulty+1)
  
  pc_map = cpu_map(numOfShips)
  user_map = user_map(numOfShips)

  game(pc_map, user_map, difficulty, numOfShips)
  
  
main_menu()
