import Piglatin

##write .py while naming files
##module name = file name and it is case sensitive
##import sys
##sys.path.append('C:\Users\Gowri\Desktop\CS_classes\7-11Batch\Cryptography')

##Function name also case-sensitive


##import X - Reference for module. X.name to refer to things in module

##from X import * - Reference to all public objects in the module - those leaving '_' ones
##can use "piglatinTranslate" to directly refer but X.name wont work, since import X is not there
##name function already there in main it is replaced
##and name is pointing to some other object - changes wont be notices

## use from import for Tkinter
##from io.drivers import zip than import io.drivers.zip - same as plain import
##but not much risk for confusion



##from X import a, b, c - only a,b,c

##X = __import__('X') - passing module name a string and assigning it to a variable in
## your current namespace
##dont know the module name before execution



##http://effbot.org/zone/import-confusion.htm

##__main__ is the name of the module if it is run as a script - on the interpreter
##>>Piglatin
## else file is imported from another module and __main__ is the module name

## this is for the case when main.py is run by the interpreter

import Piglatin_UI
from tkinter import *

if False:
    #console
    consoleObject = Piglatin_UI.ConsoleOutput()
    
else:
    #GUI
    #for passing parameter in init, frame object is aa member variable
    #frame = Tk()
    ##piglatinGUI = Piglatin_UI.GUIOutput(frame)
    #frame.mainloop()

    #GUI inherits from fram object
    #root = Tk() #not required
    
    #how does root get passed?
    Piglatin_UI.GUIOutput().mainloop()
    

##def translate(text):
##    if __name__ == "__main__":
##        translatedtext = Piglatin.piglatinTranslate("hello")
##        print("testing with hello == ", translatedtext)
##        ##this part can be used for unit tests???
##        ## print "test: square(42) ==", square(42)
##
##    else:
##        __name__ == "main"
##        translatedtext = Piglatin.piglatinTranslate(text)
##        #print(translatedtext)
##        #print("from module - main being the name of the module in this case")
##        return translatedtext
