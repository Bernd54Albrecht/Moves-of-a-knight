#! /usr/bin/python3
# Moves_of_a_knight
# By Bernd54Albrecht@gmail.com
# D-24576 Bad Bramstedt
# 29.02.2020
# Happy Birthday, Raspberry Pi
# ---------------------------------------------------

import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
from random import shuffle, choice
from time import sleep

SIZE=64

windowWidth = 8*SIZE
windowHeight = 8*SIZE
hot=False
pawns = []
player = 0
print()
print("Move the knight iot. remove the pawn(s)")
print("Be cautious - the pawn can capture the knight on a square diagonally in front!")
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
pawn = pygame.transform.smoothscale(pawn, (SIZE,SIZE))
knight = pygame.transform.smoothscale(knight, (SIZE,SIZE))
empty = pygame.transform.smoothscale(empty, (SIZE,SIZE))

def drawButtons():
 for POS in range(64):
    xPos=POS//8
    yPos=POS%8
    position=(xPos*SIZE,yPos*SIZE)
    surface.blit(board[POS], position)

def captureKnight():
  global player, pawns
  if (knightPos-9) in pawns:
    print("You are captured by the pawn in position: ",knightPos-9," = ", (knightPos-9)//8, (knightPos-9)%8) 
    pawns.remove(knightPos-9)
    pawns.append(knightPos)
  else:
    print("You are captured by the pawn in position: ",knightPos+7," = ", (knightPos+7)//8, (knightPos+7)%8)
    pawns.remove(knightPos+7)
    pawns.append(knightPos)
  print("You lost. Try again.")
  sleep(5)
  quitGame()


def move1pawn():
  global player, pawns
  if (knightPos-9) in pawns or (knightPos+7) in pawns:
    captureKnight()
  elif 7 in pawns or 15 in pawns or 23 in pawns or 31 in pawns or 39 in pawns or 47 in pawns or 55 in pawns or 63 in pawns:
    print("One pawn advanced to the eighth rank and is not immediately captured.")
    print("You lost. Try again.")
    sleep(5)
    quitGame()
  else:
    print("move 1 pawn")
    pawnselected = choice(pawns)
    print("pawnselected",pawnselected)
    if pawnselected + 1 != knightPos:
      pawns.remove(pawnselected)
      pawns.append(pawnselected+1)
      for n in range(len(pawns)):
#        print(pawns[n],pawns[n]//8,pawns[n]%8)
        board.update({ pawnselected : empty})
        board.update({ pawns[n] : pawn})
      return
    else:
      if len(pawns) > 1:
        move1pawn()
      else:
        print("End of game. Try again.")
        sleep(3)
        quitGame()

    
def handleClick(mousePos):  
  global knightPos,selxPos, selyPos, SIZE, pawns, lap, player
  player = 0
  knightxPos = knightPos//8
  knightyPos = knightPos%8
  mousexPos = int(mousePos[0]/SIZE)
  mouseyPos = int(mousePos[1]/SIZE)
  if abs(mousexPos-knightxPos)==2 and abs(mouseyPos-knightyPos)==1 or abs(mousexPos-knightxPos)==1 and abs(mouseyPos-knightyPos)==2:
    number = len(pawns)
    hit = 64
    for n in range(number):
      if pawns[n]//8 == mousexPos and (pawns[n]%8) == mouseyPos:
        hit=n
    if hit<64:
      pawns.remove(pawns[hit])
    else:
      pass
    board.update({knightPos : empty})
    knightPos = 8*mousexPos + mouseyPos
    print("New knight position is: ", knightPos, "=", knightPos//8, knightPos%8)
    board.update({knightPos : knight})    
  else:
    print("Not valid! Click again! ")
    player = 1

def quitGame():
  pygame.quit()
  sys.exit()

# Create Buttons
for i in range(64):
  board.update({ i : empty})

fields = list(range(64))
shuffle(fields)
for n in range(8):
  pawns.append(8* n + 1)
  board.update({ pawns[n] : pawn})

knightPos = 15
board.update({ knightPos : knight})

# 'main' loop
while pawns!=[]:
  if player == 0:
    move1pawn()
    player = 1
    
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
