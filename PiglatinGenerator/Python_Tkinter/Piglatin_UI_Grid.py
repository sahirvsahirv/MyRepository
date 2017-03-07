import Piglatin 
class ConsoleOutput:
    def __init__(self):
        ##analyze frequencies
        piglatinObject = Piglatin.PigLatinTranslate()
        #print(__name__)
        if __name__ == "__main__":
            #print("from commandline")
            piglatinObject.piglatinTranslate("hello")
            print("testing with hello == ", piglatintext)

            print("sentence translation")
            piglatinObject.piglatinTranslateSentence("i am gowri and you are you")

            print("frequency analysis")
            print("%s" %(piglatinObject.frquencyAnalysis()))
        elif __name__ == "Piglatin_UI":
            #print("from module - testingPiglatin_commandline being the name of the module in this case")

            texttotranslate = input("Enter text - a word: ")
            print("translated = ", piglatinObject.piglatinTranslate(texttotranslate))
            
            sentencetotranslate = input("Enter text - a sentence: ")
            print("translated text = ", piglatinObject.piglatinTranslateSentence(sentencetotranslate))

            print("frequency analysis")
            print(piglatinObject.frquencyAnalysis())

from tkinter import *


#Using the grid manager means that you create a widget,
#and use the grid method to tell the manager in which row
#and column to place them. The size of the grid doesn't have
#to be defined, because the manager automatically determines
#the best dimensions for the widgets used.

class GUIOutput(Frame):
    def __init__(self):
        #inherited from frame
        Frame.__init__(self)

        self.master.title('Piglatin Generator')

        #If you want to make the widgets as wide as the parent widget, you have to use the fill=X option: 
        lengText = Label(self.master, text="English Text")
        #Size of the label is 5 vertically - y and horizontally - x
        lengText.grid(row=0, column=0,  sticky = E)
        
        
        
        varToTranslate =  StringVar()
        text_sentencetotranslate = Entry(self.master, textvariable=varToTranslate) #Enter the translated text
        text_sentencetotranslate.grid(row=0, column=1,  sticky = E)
        
        lpiglatinText = Label(self.master, text="Translated Text")
        #sticky - expand the widget if the text is larger than widget
        lpiglatinText.grid(row=1, column=0, sticky=E)


        varTranslated =  StringVar()
        text_piglatinsentence = Entry(self.master, textvariable=varTranslated)
        text_piglatinsentence.grid(row=1, column=1, sticky = E)
        
        
        translate = Button(self.master, text = "Translate", command = lambda: self.translate(varToTranslate, varTranslated))
        translate.grid(row=2, columnspan= 2, sticky = E)

        #Disable it so that the text cannot be changed
        text_piglatinsentence.config(state=DISABLED)
        
        quitpiglatin = Button(self.master, text = "Quit",  command = self.quitCallBack)
        quitpiglatin.grid(row=2, column=4, columnspan=4,  sticky = E)
        #function pointer
        
        
    def translate(self, sentencetotranslate, piglatinsentence  ):
        #populate text box
        piglatinObject = Piglatin.PigLatinTranslate()
        piglatinsentence.set(piglatinObject.piglatinTranslateSentence(sentencetotranslate.get()))
        
        

    def quitCallBack(self):
        self.master.quit()
        self.master.destroy()




