import os
import random
import pygame
import sys

##red = (255,0,0)
##green = (0,255,0)
##blue = (0,0,255)
##darkBlue = (0,0,128)
##white = (255,255,255)
##black = (0,0,0)
##pink = (255,200,200)

#Constants
GREEN = (0, 204, 0)
WHITE = (255, 255, 255)
WIDTH = 450
HEIGHT = 650
BLUISH = (50, 50, 255)
COORDX = 0
COORDY = 100 #Gap
COORDWIDTH = 450
COORDHEIGHT = 450
SCREENBLUE = (50, 50, 128)

TILECOLOR = GREEN
TILEWIDTH = 150
TILEHEIGHT = 150
BASICFONTSIZE = 20
TEXTCOLOR = WHITE
BORDERWIDTH = 5
ROWCOLMAX = 3
SCREENSIZE = (WIDTH, HEIGHT)
GAMEBOARDCOLOR = BLUISH
GAMEBOARDCOORD = (COORDX, COORDY, COORDWIDTH, COORDHEIGHT)
SCREENCOLOR = SCREENBLUE

def terminate():
        pygame.quit()
        #This is required. If you comment this and you click quit it will give
        #an error saying pygame is not initializd but am still trying to update
        #on the next line
        #if we add this, the shell will exit for the current code and the error
        #will not be seen
        sys.exit()
        
#Had to create this since inititalization was happening multiple times
class Controller:
    board = [0]*9
    def __init__(self):
        global SCREEN, BASICFONT
        #Pygame initiation
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()

        #Get the font
        BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
        #set up display
        pygame.display.set_caption("Junior 10")
        #Screen to draw on
        SCREEN = pygame.display.set_mode(SCREENSIZE)

        #r,g,b
        SCREEN.fill(SCREENCOLOR)

        ##pygame.draw.lines(screen, color, closed, pointlist, thickness)
        ##draws a series of lines, connecting the points specified in pointlist
        ##pointlist is a list of tuples, specifying a series of points, e.g. to draw a V you might use [(100,100), (150,200), (200,100)], with closed = False
        ##closed should be either True or False, indicating whether to connect the last point back to the first
        ##thickness is the thickness of the line (in pixels).
        ##Example: pygame.draw.lines(screen, black, False, [(100,100), (150,200), (200,100)], 1)
        #pygame.draw.lines(screen, colorName, False,  [(100,100), (150,200), (200,100)], 1)

                    
        #last parameter if 0, the rectangle is filled
        #(x,y,width,height) is a Python tuple
        #x,y are the coordinates of the upper left hand corner
        #width, height are the width and height of the rectangle
        pygame.draw.rect(SCREEN, GAMEBOARDCOLOR, GAMEBOARDCOORD, 0) 

        #inner rectangle is x = 420,y = 400 - divide the square into 9 pieces
        #450/3 = 150
        #450/3 = 150
        #draw the board
        self.board = self.__getStartingBoardDS()
        print(self.board)
        self.__drawBoard(self.board, "")

    def control(self):
        running = True
    
        while running:
            self.__checkForQuit()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    #unpack the tuple
                    print("tuple = {}".format(event.pos))
                    x,y = event.pos
                    print("x ={}, y ={}".format(x,y))
                    n = self.__getSpotClicked(self.board, x, y)
                    print("Clicked tile = {}".format(n))
                    if n == -1:
                        #do nothing for now
                        return
                    
                        
                        
                            
                    
                    
            #Update the screen
            pygame.display.update()

    
    def __getSpotClicked(self, board, x, y):
        #From pixel coordinates, get where on the board it is
        for i in range(len(board)):
            #unpack the tuple
            left, top = self.__getPixelCoordinates(i)
            #Add the offset for get position in the inner screen
            tileRect =  pygame.Rect(left+COORDX, top+COORDY, TILEWIDTH, TILEHEIGHT)
            print("Tile object = {}".format(tileRect))
            if tileRect.collidepoint(x,y):
                #If collides, get the tile number
                if(i >= 0 and i <=8):
                    return i
                else:
                    print("should it ever come here?")
            else:
                #if not inside the game tile it comes here
                print("Continuing the loop")
                continue
                
      
    def __checkForQuit(self):
        """
        Checking for quit event, from the close button
        """
        #Same as passing a parameter
        ##    for event in pygame.event.get():
        ##    if event.type == pygame.QUIT:
        for event in pygame.event.get(pygame.QUIT):
            terminate()
            
    #Given a text make a surface and rectangle and display
    def __makeText(self, text, color, bgcolor, top, left):
        """
        Surface and Rect objects for positioning any text on the screen,
        given as a parameter
        """
        textSurf = BASICFONT.render(text, True, color, bgcolor)
        textRect = textSurf.get_rect()
        textRect.topleft = (top, left)
        return (textSurf, textRect)

    #Controller for drawing tiles
    """
    Private member function to draw the board
    """
    def __drawBoard(self, board, message):
        """
        Draw the board with tiles for a given filled single dimensional array-board

        Message - if exists means you can display the message in a corner
        """
        if message:
            textSurf, textRect = makeText(message, MESSAGECOLOR, BGCOLOR, 5, 5)
            SCREEN.blit(textSurf, textRect)
            
        for i in range(len(board)):
            if(board[i] != 0):
                (left, top) = self.__getPixelCoordinates(i)
                print(left, top)
                #+100 because i have left a 100 gap at the top
                self.__drawTile(left, top, COORDX, COORDY)
            else:
                continue

    #Usage: print(getStartingBoardDS.__doc__)
    #import sample
    #help(sample)
    def __getStartingBoardDS(self):
        """Data structure for poupulating the board initially with random tiles and
        combination of random numbers

        Returns the data structure

        Right now hardcoded to a combination of 4 tiles with 2 5's
        """
            
        #starting state
        #generate combinations of 10 in random
        #populate random positions max leave one square free
        #Decide algo for split and what combinations of split

        #For now choose [5] 4 times - will get 2 10's

        board = [0]*9
        #print(board)
        #tilesoccupied should never increae 8
        tilesoccupied = 0
        #Hard code for now
        #4 5'sfor 2 10's

        #index in the 1-dimensional array
        #not unique
        #random.randint(0, 8)
        #Second parameter chooses 4 items
        tiletooccupy = random.sample(range(0, 8), 4)
        #Set all the 4 random positions to 5
        for i in range(4):
            board[tiletooccupy[i]] = 5
            tilesoccupied += 1
                
        #print(tilesoccupied)
        #print(board)
        return board



    #Now turn board positions to pixel positions
    #returns the coordinated of the starting point - left,top

    #say for board[n]
    #n/3 gives row and column is n%3
    #each tile is 150*150
    #left = x =150*column
    #top = y = 150*row
    def __getPixelCoordinates(self, n):
        """
        Given the position in the board's 1 dimensional array gives the position
        in x,y coordinated for the top-left point in the tile

        Returns the coordinates
        """
        left = TILEWIDTH*(n%ROWCOLMAX)
        #Imagine not typecasting here, gives different values 
        top = TILEHEIGHT*int(n/ROWCOLMAX)
        return (left, top)

    #Draw the tile
    def __drawTile(self, tilex, tiley, adjx, adjy):
        """
        Draw the tiles with random numbers that mix to form 10
        """
        pygame.draw.rect(SCREEN, TILECOLOR, (tilex+adjx, tiley+adjy, TILEWIDTH, TILEHEIGHT), BORDERWIDTH)
        #Render images here later with the random number
        textSurf = BASICFONT.render(str(5), True, TEXTCOLOR)
        textRect = textSurf.get_rect()
        textRect.center = tilex + int(150/2) + adjx, tiley + int(150/2) + adjy
        SCREEN.blit(textSurf, textRect)
        return



def main():
    
    try:
        #Do initialization once
        controller =  Controller()
        #Event loop of the game would run
        controller.control()
        
    except SystemExit:
        terminate()

if __name__ == "__main__":
    main()
