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

SIZE=82

windowWidth = 8*SIZE
windowHeight = 8*SIZE
hot=False
pawns = []
print()
print("Move the knight iot. remove the pawn(s)")
print("Pawns do not move in this game")
print()
lap = int(input("Enter the number of pawns to start with (min 1, max 63):  "))
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
#  print(pawns[n],pawns[n]//8,pawns[n]%8)
  board.update({ pawns[n] : pawn})

knightPos = fields.pop()
#print(knightPos,knightPos//8,knightPos%8)
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

print(clicks, "clicks! Good-bye")
sleep(5)
quitGame()
