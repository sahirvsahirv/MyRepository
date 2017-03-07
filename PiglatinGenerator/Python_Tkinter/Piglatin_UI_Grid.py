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


class GUIOutput(Frame):
    def __init__(self):
        #inherited from frame
        Frame.__init__(self)

        self.geometry("170200+30+30")
        self.master.title('Piglatin Generator')

        engFrame = Frame(self)
        #If you want to make the widgets as wide as the parent widget, you have to use the fill=X option: 
        engFrame.pack(fill = X)
        lengText = Label(engFrame, text="English Text")
        #Size of the label is 5 vertically - y and horizontally - x
        lengText.place(x=20, y=30 + 30, width=120, height=25)
        
        
        varToTranslate =  StringVar()
        text_sentencetotranslate = Entry(engFrame, textvariable=varToTranslate) #Enter the translated text
        text_sentencetotranslate.pack(fill=X, padx=5, expand=True)
        
        piglatinFrame = Frame(self)
        piglatinFrame.pack(fill = X) #else take it in the old frame's place and not visible
        lpiglatinText = Label(piglatinFrame, text="Translated Text")
        lpiglatinText.pack(side=LEFT, padx=5, pady=5)


        varTranslated =  StringVar()
        text_piglatinsentence = Entry(piglatinFrame, textvariable=varTranslated)
        text_piglatinsentence.pack(fill=X, padx=5, expand=True)
        
        buttonsFrame = Frame(self)
        buttonsFrame.pack(fill = X)

        translate = Button(buttonsFrame, text = "Translate", command = lambda: self.translate(varToTranslate, varTranslated))
        translate.pack(side = LEFT, padx=10)

        #Disable it so that the text cannot be changed
        text_piglatinsentence.config(state=DISABLED)
        
        quitpiglatin = Button(buttonsFrame, text = "Quit",  command = self.quitCallBack)
        quitpiglatin.pack(side=RIGHT, padx=15)
        #function pointer
        
        
    def translate(self, sentencetotranslate, piglatinsentence  ):
        #populate text box
        piglatinObject = Piglatin.PigLatinTranslate()
        piglatinsentence.set(piglatinObject.piglatinTranslateSentence(sentencetotranslate.get()))
        
        

    def quitCallBack(self):
        self.master.quit()
        self.master.destroy()




