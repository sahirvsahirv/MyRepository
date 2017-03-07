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

#Creates a new frame everytime and does not give the flexibility to use different
#parameter options
##def frame(root, side):
##    w = Frame(root)
##    w.pack(side = side, expand = YES, fill = BOTH)
##    return w

#myvar.trace - Debug and print



class GUIOutput(Frame):
    def __init__(self):
        #inherited from frame
        Frame.__init__(self)
        
        self.pack(expand =  YES, fill = BOTH)
        self.master.title('Piglatin Generator')

        #Using the same frame all through out and the window expands horizontally
        piglatinFrame = Frame(self)
        piglatinFrame.pack(fill = X)
        lengText = Label(piglatinFrame, text="English Text")        
        lengText.pack(side=LEFT, padx=5, pady=5)
        
        #Removing the neccessity of lambda function, by making the text boxes a member variable
        varToTranslate =  StringVar()
        text_sentencetotranslate = Entry(piglatinFrame, textvariable=varToTranslate) #Enter the translated text
        text_sentencetotranslate.pack(side=LEFT, padx=5, expand=True)

        
        #piglatinFrame = Frame(self)
        #piglatinFrame.pack(fill = X) #else take it in the old frame's place and not visible
        lpiglatinText = Label(piglatinFrame, text="Translated Text")
        lpiglatinText.pack(side=LEFT, padx=5, pady=5)


        varTranslated =  StringVar()
        text_piglatinsentence = Entry(piglatinFrame, textvariable=varTranslated)
        text_piglatinsentence.pack(side=LEFT, padx=5, expand=True)
        
        
        #function pointer
        #Removing the neccessity of lambda function, by making the text boxes a member variable
        translate = Button(piglatinFrame, text = "Translate", command = lambda: self.translate(varToTranslate, varTranslated))
        translate.pack(side=LEFT, padx=10)
        #Disable it so that the text cannot be changed
        text_piglatinsentence.config(state=DISABLED)

        
        
        quitpiglatin = Button(piglatinFrame, text = "Quit",  command = self.quitCallBack)
        quitpiglatin.pack(side=LEFT, padx=10)
        

        
    def translate(self, sentencetotranslate, piglatinsentence  ):
        #populate text box
        piglatinObject = Piglatin.PigLatinTranslate()
        piglatinsentence.set(piglatinObject.piglatinTranslateSentence(sentencetotranslate.get()))


    def quitCallBack(self):
        self.master.quit()
        self.master.destroy()




