#git checkout -b memorygame
#git add memory.py
#git commit -m "memory game"
#git push origin memorygame

#Hint to the windows manage through the environment var
#that the window needs to be centered. This can be ignored
#by windows manager
import os
os.environ["SDL_VIDEO_CENTERED"] = "1"

import pygame
"""
Write algorithm
Explain python concepts
Tuple
List of lists
Object instantiation from an imported library
calling functtions on that namespace and oject
Tuples to maintain data like colors
Usage of constants effectively to reuse numbers and for clarity in code
Iteration and instantiation of arrays

1. Init
2. Font
3. Caption
4. Get screen object based on screen size
5. color the screen
6. Maintain DS - random, tuples, 2 dim list populate
7. draw items you need - 4 tiles, color matched
8. play music
9. show tiles once and Flip the tiles

Event loop
Use of booleans to maintain state
how events work
from the event pos get the tile clicked
collidepoint and function for topcoordinated to get rec coord
if it is just hovering highlight
In the beginning of the loop, erase the highlight, on each hover else the hightlight remains
While erasing, keep in mind clicked tiles
    Redraw the background logo
    Redraw the tiles
    Not the revealed ones

Maintain DS for clicked tiles
and in the beginning of the loop redraw board with all tiles upturned except for
clicked tiles

Event loop on click, turn 1 tile
Turn second, if second is a match play another music
Else upturn
If match proceed for the next 2, in a similar fashion
"""
#initialize pygame - call the constructor
pygame.init()

#set the font
font = pygame.font.Font('freesansbold.ttf', 20)
#caption
pygame.display.set_caption("Memory game")

#screen object to display
#resolution = (0,0) tuple - immutable data structure
BOARDWIDTH = 2
BOARDHEIGHT = 2
TILEWIDTH = 150
TILEHEIGHT = 150
screen = pygame.display.set_mode((TILEWIDTH*BOARDWIDTH, TILEHEIGHT*BOARDHEIGHT))

#fill the screen with a color
#http://www.rapidtables.com/web/color/RGB_Color.htm

PINK   = (255,   0, 255)
#No need to fill since i am drawing a rect to fill to get the image in center
screen.fill(PINK)

#colors
RED = (255, 0 , 0)
BLUE = (0,0,255)

#color tuple
ALLCOLORS = (RED, BLUE)

import random

#get randomly 1 and 0 twice
#Do it twice and repeat
#Get random color - 2 colors [0,1) 0/1, 2 exclusive

#TODO: Read up on the different algorithms to do this

colorarr = []
#need 2 random colors - for will give me two
for i in range(0, BOARDWIDTH):
    #includes both end points
    color = random.randint(0, BOARDWIDTH-1)
    colorarr.append(ALLCOLORS[color])
    
#Pair it up to make 4
#colorarr has 2
copylist = list(colorarr)
#merge both into colorarr
colorarr = colorarr + copylist
print("Non - Random array of 4 colors = {}".format(colorarr))
random.shuffle(colorarr)
print("Random array of 4 colors = {}".format(colorarr))

#data structure 2 dim - list of lists
#2 image for 4 tiles - randomly distribute
#new DS to store 2 copies of 2 randomly generated images/colors
#nested loop will just pick from this new array
board = []
colorcount = 0
for col in range(BOARDWIDTH):
    columnarr = []
    for row in range(BOARDHEIGHT):
        columnarr.append(colorarr[colorcount])
        colorcount+=1
    board.append(columnarr)
print("Board = {}".format(board))

#draw the board
cgbackground = pygame.image.load('cglogobg.png')
tilelogo = pygame.image.load('soccer-icon.png')

#center the background image
rect = (0, 0, TILEWIDTH*BOARDWIDTH, TILEHEIGHT*BOARDHEIGHT )
rectObject = pygame.draw.rect(screen,BLUE,rect)
rectObject = cgbackground.get_rect(center=rectObject.center)

#draw a surface onto another
screen.blit(cgbackground, rectObject)

#draw tiles

#margins so that tiles dont stick to each other
XMARGIN = 5
YMARGIN = 5
#On left and right and top and bottom
GAP = 2

#TODO: Move to a function drawing tiles with logo
#Draw the board without revealed boxes
for row in range(BOARDHEIGHT):
    for col in range(BOARDWIDTH):
        #rect starting position
        rect = ( ((col*TILEWIDTH)+XMARGIN), ((row*TILEHEIGHT)+YMARGIN),TILEWIDTH-(GAP*XMARGIN),TILEHEIGHT-(GAP*YMARGIN))
        rectObject = pygame.draw.rect(screen, PINK, rect)
        #Logo to the center of the tile
        rectObject = tilelogo.get_rect(center = rectObject.center)
        screen.blit(tilelogo, rectObject)

#do this to display on the screen, else you see a black screen always
pygame.display.update()

#Now recognise events
#Show all the tiles in the beginning
#1. Move the cursor and highlight the tile
#2. On click flip the tile
#3. on second click, if no match flip it back again
#4. if match keep it and dont let the user click it again
#5. monitor exit

#TODO: game animation, show once and flip it immediately

GRAY   = (100,   100, 100) #even if change my color, have to change only at 2 places
HIGHLIGHTCOLOR = GRAY
#for sys.exit()
import sys

#Keep a track Revealed boxes
revealedBoxes = []
for i in range(TILEWIDTH):
    #0 is that it is not revealed
    revealedBoxes.append([0] * TILEHEIGHT)

#continuously monitor
while True:
    boolMouseCicked = False

    #Draw the board again so that highlighting is gone
    #TODO: Move to a function - drawing the board
    #Load the image to remove highlighting
    #TODO: Move to a function :Loading the image and displaying
    #center the background image
    rectBG = (0, 0, TILEWIDTH*BOARDWIDTH, TILEHEIGHT*BOARDHEIGHT )
    rectObject = pygame.draw.rect(screen,BLUE,rectBG)
    rectObject = cgbackground.get_rect(center=rectObject.center)
    #draw a surface onto another
    screen.blit(cgbackground, rectObject)

    #Draw the board without revealed boxes
    for row in range(BOARDHEIGHT):
        for col in range(BOARDWIDTH):
            #rect starting position
            rect = ( ((col*TILEWIDTH)+XMARGIN), ((row*TILEHEIGHT)+YMARGIN),TILEWIDTH-(GAP*XMARGIN),TILEHEIGHT-(GAP*YMARGIN))
            #revealed for the tile does not have 0, then show the color
            #pick up the color from the board data structure
            if revealedBoxes[row][col]:
                rectObject = pygame.draw.rect(screen, board[row][col], rect)
            else:
                #print("am here")
                #Draw the pink tile with football
                rectObject = pygame.draw.rect(screen, PINK, rect)
                #Logo to the center of the tile
                rectObject = tilelogo.get_rect(center = rectObject.center)
                screen.blit(tilelogo, rectObject)
    #Re-Drawing board so that highlighting and flipping is gone- OVER
                
    for event in pygame.event.get():
        #(quit and mouse) up or (esc and key up)
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key==pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            #print("mouse moved to another tile")
            mousex,mousey = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            #print("clicked the mouse")
            boolMouseCicked = True

    #still inside while, post identify events, do the needful for each event

    #from the mouse position identify which tile is it?
    for row in range(BOARDHEIGHT):
        for col in range(BOARDWIDTH):
            #Same used while drawing the logo
            #TODO: move into a function
            rect = ( ((col*TILEWIDTH)+XMARGIN), ((row*TILEHEIGHT)+YMARGIN),TILEWIDTH-(GAP*XMARGIN),TILEHEIGHT-(GAP*YMARGIN))
            rectObject = pygame.Rect(rect)
            if rectObject.collidepoint(mousex, mousey):
                #valid collision
                if(row != None and col != None):
                    #if not already flipped, revealed
                    #highlight the box
                        #print("highlighting the tile, move into")
                        #borderwidth = 4
                        #TODO: Move to a function
                        left = ((col*TILEWIDTH))
                        top = ((row*TILEHEIGHT))
                        width = TILEWIDTH
                        height = TILEHEIGHT
                        rect = (left, top, width, height)
                        #print(rect)
                        pygame.draw.rect(screen, HIGHLIGHTCOLOR, rect, 4)

    #update inside he for to see the changes made to highlight the tile etc
    pygame.display.update()
                    #if not revealed and mouse clicked
                        #print("reveal the box data")
                        #Keep track of whether the box has been revealed
                        #if only one clicked
                            #firstselection = (row,col)
                        #else
                            #check if there is a match
                            #if no match cover them again
                            #revealed boxes = false
                        #else
                            #if all boxes have been revealed
                            #game over
#Play music
#pygame.mixer.music.load('background.mp3')
#infinitely
#pygame.mixer.music.play(-1)
