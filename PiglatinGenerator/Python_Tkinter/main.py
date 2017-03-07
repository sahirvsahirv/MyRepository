import Piglatin
#import Piglatin_UI
import Piglatin_UI_withoutFrames
from tkinter import *

if False:
    #console
    consoleObject = Piglatin_UI.ConsoleOutput()
    
else:
    #GUI
    #Piglatin_UI.GUIOutput().mainloop()
    Piglatin_UI_withoutFrames.GUIOutput().mainloop()
