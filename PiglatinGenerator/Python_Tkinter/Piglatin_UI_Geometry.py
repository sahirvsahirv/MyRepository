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
import random

class GUIOutput(Frame):
    def __init__(self):
        #inherited from frame
        frame = Frame.__init__(self)
        #Width*height + x_offset + y_offset - formatted string
        self.master.geometry("400x200+30+30")
        self.master.title('Piglatin Generator')

        #If you want to make the widgets as wide as the parent widget, you have to use the fill=X option: 
        lengText = Label(frame, text="English Text")
        #Size of the label is 5 vertically - y and horizontally - x
        lengText.place(x=50, y=30, width=120, height=25)
        
        
        varToTranslate =  StringVar()
        text_sentencetotranslate = Entry(frame, textvariable=varToTranslate) #Enter the translated text
        text_sentencetotranslate.place(x=50 + 100 + 50, y=30, width=120, height=25)
        
        lpiglatinText = Label(frame, text="Translated Text")
        lpiglatinText.place(x=50, y=30 + 30 + 30, width=120, height=25)


        varTranslated =  StringVar()
        text_piglatinsentence = Entry(frame, textvariable=varTranslated)
        text_piglatinsentence.place(x=50 + 100 + 50, y=30 + 30 + 30, width=120, height=25)
        
        

        translate = Button(frame, text = "Translate", command = lambda: self.translate(varToTranslate, varTranslated))
        translate.place(x=50, y=30*5, width=120, height=25)

        #Disable it so that the text cannot be changed
        text_piglatinsentence.config(state=DISABLED)
        
        quitpiglatin = Button(frame, text = "Quit",  command = self.quitCallBack)
        quitpiglatin.place(x=200, y=30*5, width=120, height=25)
        #function pointer
        
        
    def translate(self, sentencetotranslate, piglatinsentence  ):
        #populate text box
        piglatinObject = Piglatin.PigLatinTranslate()
        piglatinsentence.set(piglatinObject.piglatinTranslateSentence(sentencetotranslate.get()))
        
        

    def quitCallBack(self):
        self.master.quit()
        self.master.destroy()




