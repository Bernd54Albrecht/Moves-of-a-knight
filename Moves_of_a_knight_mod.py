#! /usr/bin/python3
# Moves_of_a_knight
# By Bernd54Albrecht@gmail.com
# D-24576 Bad Bramstedt
# 29.02.2020
# Happy birthday, Raspberry Pi
# ---------------------------------------------------

import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
from random import shuffle
from time import sleep
from itertools import permutations
from math import factorial
import _thread

SIZE=82

windowWidth = 8*SIZE
windowHeight = 8*SIZE
hot=False
pawns = []
print()
print("Move the knight iot. remove the pawn(s)")
print("Pawns do not move in this game")
print()
lap = int(input("Enter the number of pawns to start with (min 1, max 9):  "))
print()
clicks = 0

pygame.init()
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Moves of a knight - Rösselsprung')

board = {}

# Set up the images.
pawn=pygame.image.load("pawn52.png")
knight=pygame.image.load("knight52.png")
empty=pygame.image.load("empty52.png")

# Use smoothscale() to adjust the images:
empty = pygame.transform.smoothscale(empty, (SIZE,SIZE))
pawn = pygame.transform.smoothscale(pawn, (SIZE,SIZE))
knight = pygame.transform.smoothscale(knight, (SIZE,SIZE))


# mousePosition = None

def drawButtons():

  for POS in range(64):
    xPos=POS//8
    yPos=POS%8
    position=(xPos*SIZE,yPos*SIZE)
    surface.blit(board[POS], position)

def handleClick(mousePos):  
  global knightPos,selxPos, selyPos, SIZE, pawns, lap
  knightxPos = knightPos//8
  knightyPos = knightPos%8
  mousexPos = int(mousePos[0]/SIZE)
  mouseyPos = int(mousePos[1]/SIZE)
#  print(mousePos, mousexPos, mouseyPos)
  if abs(mousexPos-knightxPos)==2 and abs(mouseyPos-knightyPos)==1 or abs(mousexPos-knightxPos)==1 and abs(mouseyPos-knightyPos)==2:
    number = len(pawns)
    hit = 64
    for n in range(number):
#      print(n, number)
#      print(pawns[n]//8,pawns[n]%8,mousexPos, mouseyPos)
      if pawns[n]//8 == mousexPos and (pawns[n]%8) == mouseyPos:
        hit=n
    if hit<64:
      pawns.remove(pawns[hit])
    else:
      pass
     
    board.update({knightPos : empty})
    knightPos = 8*mousexPos + mouseyPos
    board.update({knightPos : knight})
        
  else:
    print("Not valid! Click again! ")


            
## Functions for die Computation of Minimum Moves
## computed in a thread parallel to the game

def permutation(n):
  # path will always start at knightPos = 1
  # position of knight[0] = 2; therfore always add 2 to index
  p = list(range(2,n+2))
#  print("list p = ", p)
  P = list(permutations(p))
#  print("List of Permutations = ", P)
  Perm = P[:]
  for i in range(factorial(n)):
    Perm[i] = [1] + list(P[i])
#    print("List of Permutations = ",i, Perm[i])
  return Perm

def assign_weights(lap,knightPos,pawns):
  global minW, best
  Matrix = [[0,3,2,3,2,3,4,5],[3,2,1,2,3,4,3,4],[2,1,4,3,2,3,4,5],
            [3,2,3,2,3,4,3,4],[2,3,2,3,4,3,4,5],[3,4,3,4,3,4,5,4],
            [4,3,4,3,4,5,4,5],[5,4,5,4,5,4,5,6]]
  Permutations = permutation(lap)
  numberPermutations = len(Permutations)
  t = [knightPos] + pawns
#  print("numberPermutations = ",numberPermutations)
#  print("Tokens = ",t)
  minW = 9999
  best = Permutations[0]
  for i in range(numberPermutations):
    l = len(Permutations[i])
    perm = Permutations[i]
#    print("perm = ",perm)
    sumW = 0
    for k in range(l-1):
#      print("k = ",k, "k+1 = ",k+1)
#      print("perm[k] = ", perm[k], "perm[k+1] = ", perm[k+1])      
#      print("t[perm[k]-1] = ", t[perm[k]-1], "t[perm[k+1]-1] = ", t[perm[k+1]-1])

      dc = abs(t[perm[k]-1]//8 -t[perm[k+1]-1]//8)
      dr = abs(t[perm[k]-1]%8 -t[perm[k+1]-1]%8)
#      print("dc = ",dc," dr = ",dr)
      dw = Matrix[dr][dc]
#      print("dw = ", dw)
      sumW = sumW + dw
#    print("sumW",sumW)
    if sumW < minW:
#      print("kleiner?")
      minW = sumW
      best = perm
    else:
      pass
#    print("minW",minW)
#    print()
#  print("minW",minW)    
#  print("Best Path: ", best)
#  print()


def quitGame():
  pygame.quit()
  sys.exit()

# Create Buttons
for i in range(64):
  board.update({ i : empty})

fields = list(range(64))
shuffle(fields)
for n in range(lap):
  pawns.append(fields.pop())
  print(pawns[n],pawns[n]//8,pawns[n]%8)
  board.update({ pawns[n] : pawn})
Pawns = pawns[:]
knightPos = fields.pop()
KnightPos = knightPos
print(knightPos,knightPos//8,knightPos%8)

_thread.start_new_thread(assign_weights,(lap,knightPos,pawns))




board.update({ knightPos : knight})

# 'main' loop
while pawns!=[]:
#  print(pawns)
  surface.fill((255,255,255))
  mousePos = pygame.mouse.get_pos()

  for event in GAME_EVENTS.get():

    if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_ESCAPE:
        quitGame()

    if event.type == GAME_GLOBALS.QUIT:
      quitGame()

    if event.type == pygame.MOUSEBUTTONUP:
      clicks +=1
      handleClick(mousePos)

  drawButtons()

  pygame.display.update()

print("You needed ",clicks, "clicks! Shortest path requires ",minW,"clicks")
##print("First permutation with shortest path is: ")
##print("Knight ", KnightPos, "(",KnightPos//8,KnightPos%8,")")
##print("Pawns:")
##for n in range(1,lap+1):
##  p = Pawns[best[n]-2]
##  print(p,"(",p//8,p%8,")")
print("Good-bye")
sleep(5)
quitGame()
