import os
import random
import pygame
import sys
import pygame.time

##red = (255,0,0)
##green = (0,255,0)
##blue = (0,0,255)
##darkBlue = (0,0,128)
##white = (255,255,255)
##black = (0,0,0)
##pink = (255,200,200)

#Constants
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 450
HEIGHT = 650
BLUISH = (50, 50, 255)
COORDX = 0
COORDY = 100 #Gap
COORDWIDTH = 450
COORDHEIGHT = 450
SCREENBLUE = (50, 50, 128)
JUSTTEN = 10
COMB1 = [9,1]
COMB2 = [8,2]
COMB3 = [7,3]
COMB4 = [6,4]
COMB5 = [5,5]
PAIRSIZE = 2
GAMEOVERXPOS = 325
GAMEOVERYPOS = 225

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
MESSAGECOLOR = RED
MESSAGEBGCOLOR = BLACK
SCREENCOLOR = SCREENBLUE
BOARDSIZE = 3
NOBORDER = 0

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
        board = [0]*(BOARDSIZE*BOARDSIZE)
        twoDimBoard = [[0]*BOARDSIZE]*BOARDSIZE
        
        
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
                reDraw = False
                self.__drawBoard(self.board, "", reDraw)

        def control(self):
                running = True
                #making them outside the scope of the if conditions and giving it scope inside the
                #function so that it can be accessed throughout inside control
                clickedTile = -1
                movedToTile = -1
                while running:
                        self.__checkForQuit()

                        for event in pygame.event.get():
                                #Detect a move
                                #make it simple only one square can be moved
                                if(event.type == pygame.MOUSEBUTTONUP and pygame.MOUSEMOTION and pygame.MOUSEBUTTONDOWN):
                                        #unpack the tuple
                                        print("tuple = {}".format(event.pos))
                                        x,y = event.pos
                                        print("x ={}, y ={}".format(x,y))
                                        movedToTile = self.__getSpotClicked(self.board, x, y)
                                        print("Moved to tile = {}".format(movedToTile))
                                        #No returning -1 any more. Continuiing till the user clicks something
                                        ##                    if n == -1:
                                        ##do nothing for now
                                        ##return
                                        gameOver = self.__checkIfEmptyAndMove(clickedTile, movedToTile)
                                        if(gameOver):
                                                #TODO:display game over message
                                                reDraw = False
                                                self.__drawBoard(self.board, "Game Over", reDraw)
                                                #For modularity shifted drawing board from "__checkIfEmptyAndMove"
                                                #to here
                                                #Let the clock tick for 60 seconds before re-drawing
                                                #clock = pygame.time.Clock()
                                                #clock.tick(60)
                                                #Get the new board and Draw the board again
                                                self.board = self.__getStartingBoardDS()
                                                print(self.board)
                                                print("Board = {}".format(self.board))
                                                #Pass another parameter to know it is re-drawing, to save effort of erasing
                                                reDraw = True
                                                self.__drawBoard(self.board, "", reDraw)
                                elif(event.type ==  pygame.MOUSEBUTTONDOWN):
                                        #set a boolean flag as to it was pressed and get the cell in which it happened
                                        x,y = event.pos
                                        print("x ={}, y ={}".format(x,y))
                                        clickedTile = self.__getSpotClicked(self.board, x, y)
                                        print("Clicked tile = {}".format(clickedTile))
                                        
                                #Update the screen
                                pygame.display.update()
                                #pygame.display.flip()

        def __slideInto(self, oldPos, newPos, newNumber):
                (leftold, topold) = self.__getPixelCoordinates(oldPos)
                (left, top) = self.__getPixelCoordinates(newPos)
                print("Erase coordinates {}".format(leftold, topold))
                print("Slide into coordinates {}".format(left, top))
                
                #Erase old and erase where you slide into as well
                print("Erasing old tile")
                self.__drawTile(leftold, topold, COORDX, COORDY, 0)
                print("Erasing where you are sliding into")
                self.__drawTile(left, top, COORDX, COORDY, 0)
                #+100 because i have left a 100 gap at the top
                print("redrawing with new value")
                self.__drawTile(left, top, COORDX, COORDY, newNumber)
                
                print("Done")
                
                return
        
        def __turnBoardToTwoDim(self):
                #board is a member variable
                for row in range(BOARDSIZE):
                        for col in range(BOARDSIZE):
                                self.twoDimBoard[row][col] = self.board[row*BOARDSIZE+col]
                return
        
        def __checkIfValidMove(self, oldPos, newPos):
                print("oldPos = {} , newPos = {}".format(oldPos, newPos))
                #not one of the 9 grids
                if((newPos == None) or (oldPos == None)):
                        return False
                print("board value at position oldPos = {}".format(self.board[oldPos]))
                #If moving from an empty position
                if(self.board[oldPos] == 0):
                        #TODO: message box on the screen
                        print("Display message - choose a tile to move")
                        return False
                self.__turnBoardToTwoDim()
                #Get row and column from BoardPosition
                oldrow = int(oldPos/BOARDSIZE)
                oldcol = oldPos%BOARDSIZE
                newrow = int(newPos/BOARDSIZE)
                newcol = newPos%BOARDSIZE

                #possible new positions
                #oldrow-1, oldcol. Position = (oldrow-1)*BOARDSIZE+col
                #oldrow+1, oldcol. Position = (oldrow+1)*BOARDSIZE+col
                #oldrow, oldcol-1. Position = oldrow*BOARDSIZE+(col-1)
                #oldrow, oldcol+1. Position = oldrow*BOARDSIZE+(col+1)

                print("possible pos = {} and newPos = {}".format(((oldrow-1)*BOARDSIZE+oldcol), newPos))
                print("possible pos = {} and newPos = {}".format(((oldrow+1)*BOARDSIZE+oldcol), newPos))
                print("possible pos = {} and newPos = {}".format((oldrow*BOARDSIZE+(oldcol-1)), newPos))
                print("possible pos = {} and newPos = {}".format((oldrow*BOARDSIZE+(oldcol+1)), newPos))
                #range(0,11) gives 0-10
                if( ( ((oldrow-1)*BOARDSIZE+oldcol) in range(0,len(self.board))) and (newPos == ((oldrow-1)*BOARDSIZE+oldcol)) ):
                        print("returning is a valid move")
                        return True
                elif( ( ((oldrow+1)*BOARDSIZE+oldcol) in range(0,len(self.board))) and (newPos == ((oldrow+1)*BOARDSIZE+oldcol)) ):
                        print("returning is a valid move")
                        return True
                elif( ((oldrow*BOARDSIZE+(oldcol-1)) in range(0,len(self.board))) and (newPos == (oldrow*BOARDSIZE+(oldcol-1)))):
                        print("returning is a valid move")
                        return True
                elif( ((oldrow*BOARDSIZE+(oldcol+1)) in range(0,len(self.board))) and (newPos == (oldrow*BOARDSIZE+(oldcol+1))) ):
                        print("returning is a valid move")
                        return True
                else:
                        print("returning is not a valid move")
                        return False
                

        def __checkIfEmpty(self, oldPos, newPos):
                #not one of the 9 grids
                if((newPos == None) or (oldPos == None)):
                        return False
                print("board value to position newPos = {}".format(self.board[newPos]))
                #If moving to an empty position
                if(self.board[newPos] == 0):
                        return True
                return False

        def __checkIfValidJoinTiles(self, oldPos, newPos):
                #Check if all are 10's and draw a new tile
                #Let 10's move around but and slide into
                
                #not one of the 9 grids
                if((newPos == None) or (oldPos == None)):
                        return False
                print("board value to position newPos = {}".format(self.board[oldPos]+self.board[newPos]))
                if((self.board[oldPos]+self.board[newPos]) > 10):
                        #Erroneus move - do nothing
                        return False
                elif((self.board[oldPos]+self.board[newPos]) == 10):
                        print("10 done")
                        #change the board and re-draw the tile
                        #TODO: make it non clickable
                        return True
                        
                #If moving to a valid positon < 10
                else:
                        print("Valid less than 10")
                        #Redraw the tile to new value
                        #change the board and maintain a new board perhaps?
                        return True
                return False

        def __checkifGameOver(self):
                for i in range(0, len(self.board)):
                        if((self.board[i] != 10) and (self.board[i] != 0)):
                                return False
                return True
        
        def __checkIfEmptyAndMove(self, oldPos, newPos):
                #Algorithm
                #check if valid move - make it simple - only one cell allowed
                #check if empty - move if empty
                #if not empty add and make it 10 or show error and stay at the same place
                if(self.__checkIfValidMove(oldPos, newPos)):
                        print("Valid move")
                        if(self.__checkIfEmpty(oldPos, newPos)):
                                self.board[newPos] = self.board[oldPos]
                                #empty it
                                self.board[oldPos] = 0
                                self.__slideInto(oldPos, newPos, self.board[newPos])
                        else:
                                #Add board positions
                                if(self.__checkIfValidJoinTiles(oldPos, newPos)):
                                        
                                        self.board[newPos] = self.board[oldPos]+self.board[newPos]
                                        self.board[oldPos] = 0
                                        #empty it
                                        self.board[oldPos] = 0
                                        self.__slideInto(oldPos, newPos, self.board[newPos])
                                        #Extra time for the user to realise combinations are done
                                        clock = pygame.time.Clock()
                                        clock.tick(10)
                                        print("Checking if game is over")
                                        print("Board = {}".format(self.board))
                                        if(self.__checkifGameOver()):
                                                #draw board again
                                                #self.board = self.__getStartingBoardDS()
                                                #print(self.board)
                                                #Print message woth ok
                                                #Erase previous tile
                                                #Don't draw here
                                                #self.__drawBoard(self.board, "")
                                                
                                                print("Game over")
                                                return True
                                        else:
                                                return False
                                                print("Game is not over")
                                else:
                                        #do nothing
                                        #ToDO: probably show a message and stay at the same place
                                        return False
                else:
                        print("Coming in not a valid move's else")
                        #TODO: Display error message and stay at same place
                        return False
                        
            

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
                                if(i in range(0, len(board))):
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
        def __drawBoard(self, board, message, reDraw):
                """
                Draw the board with tiles for a given filled single dimensional array-board

                Message - if exists means you can display the message in a corner
                """
                if message:
                        textSurf, textRect = self.__makeText(message, MESSAGECOLOR, MESSAGEBGCOLOR, GAMEOVERYPOS, GAMEOVERXPOS)
                        SCREEN.blit(textSurf, textRect)
                        #Time the clock and redraw new combination of tiles where you re-start
                        #clock = pygame.time.Clock()
                        #clock.tick(30)
                        return
                #There was no else here and for was inside the if, for should be next to drawBoard
                #without the else
                else:
                        for i in range(len(board)):
                                if(board[i] != 0):
                                        (left, top) = self.__getPixelCoordinates(i)
                                        print(left, top)
                                        #+100 because i have left a 100 gap at the top
                                        #First time erase not required
                                        #Erase old tile for a new game situation

                                        #Erase the position you are drawing into, only if you are re-drawing
                                        #saving effort
                                        if(reDraw):
                                                print("Erasing old tile")
                                                #BUG resolved:Passing 0 for draw tile to erase
                                                self.__drawTile(left, top, COORDX, COORDY, 0)
                                                
                                        #Drawing the new board position
                                        self.__drawTile(left, top, COORDX, COORDY, board[i])
                                else:
                                        continue

        def __nestedListstoList(self, nestedListOfPairs):
                """
                Convert nested list to a single dim list
                """
                print("Nested list of pairs = {}".format(nestedListOfPairs))
                singleList = [0]*(len(nestedListOfPairs)*PAIRSIZE)
                listiter = 0
                print(singleList)
                for row in range(len(nestedListOfPairs)):
                        for col in range(PAIRSIZE):
                                print("lisiter = {}, row = {}. col = {}".format(listiter, row, col))
                                singleList[listiter] = nestedListOfPairs[row][col]
                                listiter = listiter + 1
                print("populated single = {}".format(singleList))
                return singleList
        #Usage: print(getStartingBoardDS.__doc__)
        #import sample
        #help(sample)
        def __getStartingBoardDS(self):
                """Data structure for poupulating the board initially with random tiles and
                combination of random numbers

                Returns the data structure

                Right now hardcoded to a combination of 4 tiles with 2 5's
                """
                #Algorithm: Start with 2 numbers any of COMB1 - COMB5
                #When all are 10, take 4, pick 2 of COMB1-COMB5
                #Next level pick 6, 3 of all
                #Next level pick 8, 4 of all
                #OR in random 2,4,6,8 of all 5 
                
                #starting state
                #generate combinations of 10 in random
                #populate random positions max leave one square free
                #Decide algo for split and what combinations of split

                #For now choose [5] 4 times - will get 2 10's

                board = [0]*(BOARDSIZE*BOARDSIZE)
                #print(board)
                #tilesoccupied should never increae 8
                tilesoccupied = 0
                #Hard code for now
                #4 5'sfor 2 10's

                #index in the 1-dimensional array
                #not unique
                #random.randint(0, 8)
                #Second parameter chooses 4 items

                #Since we have items in pairs
                noOfPairs = random.randrange(1, int(len(board)/2))
                #sample 1st param = population, set of 5
                #2nd param = k set of items
                tiletooccupy = random.sample([COMB1, COMB2, COMB3, COMB4, COMB5], noOfPairs)
                #print("Sample of 4 fives = {}".format(tiletooccupy))
                #Set all the 4 random positions to 5

                #now i need a random sample of board positions
                tilesOccupied =  noOfPairs*PAIRSIZE
                print("Tiles occupied = {}".format(tilesOccupied))
                #Turn list of lists to a list of integers
                boardlist = self.__nestedListstoList(tiletooccupy)
                #returns a number from 1 to tilesOccupied (2/4/6/8)
                for i in range(0, tilesOccupied):
                        #BUG: Unique board positions
                        boardposition = random.randint(0, ((BOARDSIZE*BOARDSIZE)-1) )
                        #Create another till you get a new one
                        while(board[boardposition] != 0):
                                print("Choosing board position again")
                                boardposition = random.randint(0, ((BOARDSIZE*BOARDSIZE)-1) )
                        print("Boardposition = {} and value = {}".format(boardposition, boardlist[i]))
                        board[boardposition] = boardlist[i]
                        tilesoccupied += 1

######                for i in range(tilesOccupied):
######                        board[tiletooccupy[i]] = 5
######                        tilesoccupied += 1

                print(tilesoccupied)
                print(board)
                #If there is one more tab here - return will go inside the for and return
                #after 1 5 itself
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
        def __drawTile(self, tilex, tiley, adjx, adjy, tileNumber):
                """
                Draw the tiles with random numbers that mix to form 10
                """
                #Erase
                if(tileNumber == 0):
                        print("Erase the tile")
                        pygame.draw.rect(SCREEN, BLUISH, (tilex+adjx, tiley+adjy, TILEWIDTH, TILEHEIGHT), NOBORDER)
                        #Render images here later with the random number
                        #textSurf = BASICFONT.render("", True, TEXTCOLOR)
                        #textRect = textSurf.get_rect()
                        #textRect.center = tilex + int(TILEWIDTH/2) + adjx, tiley + int(TILEHEIGHT/2) + adjy
                        #SCREEN.blit(textSurf, textRect)
                else:
                        pygame.draw.rect(SCREEN, TILECOLOR, (tilex+adjx, tiley+adjy, TILEWIDTH, TILEHEIGHT), BORDERWIDTH)
                        #Render images here later with the random number
                        textSurf = BASICFONT.render(str(tileNumber), True, TEXTCOLOR)
                        textRect = textSurf.get_rect()
                        textRect.center = tilex + int(TILEWIDTH/2) + adjx, tiley + int(TILEHEIGHT/2) + adjy
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
