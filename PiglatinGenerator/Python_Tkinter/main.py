import Piglatin
#import Piglatin_UI
#import Piglatin_UI_withoutFrames
#import Piglatin_UI_withoutLambda
#import Piglatin_UI_Geometry
import Piglatin_UI_Grid

from tkinter import *

#Shows all GUI's one by one
if False:
    #console
    consoleObject = Piglatin_UI.ConsoleOutput()
    
else:
    #GUI

    #Packing positioning relative to each other
    
    #Piglatin_UI.GUIOutput().mainloop()
    #Piglatin_UI_withoutFrames.GUIOutput().mainloop()
    #Piglatin_UI_Geometry.GUIOutput().mainloop()
    Piglatin_UI_Grid.GUIOutput().mainloop()
    
    #Only UI - without a class - to eliminate lambda
    #should run automatically through import - comment out everything for this case
    
