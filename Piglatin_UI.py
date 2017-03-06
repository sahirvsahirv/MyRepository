##testing main
##http://pythonicprose.blogspot.in/2009/09/python-pig-latin-generator.html
##List slicing

##when to use lists
##mixed collection of data types
##ordered data
##size is flexible
##maintains indexes like arrays
##list implementation of stack of Queue
##repeats possible - use sets for no repeats

##frozen set - here vowels should be a frozen set
##mathematical manipulation


##tuples dont change - can contain mutable data
##vowels dont change, can store pairs or triples

##dictionary key can change unlike lists and arrays and immutable and unique
##values can change
##each word in a sentence is the key
##fast lookup of data on the key and data being constantly modifies

##use dictionary - tkinter and OOP
##"hello, am here and you are there and we are here and they are there"

#import main

##texttotranslate = input("Enter text - a word: ")
##print("translated = ", main.translate(texttotranslate))
##
##sentencetotranslate = input("Enter text - a sentence: ")
##print("check the sentence to translate = ", sentencetotranslate)
##piglatinsentence = ""
##
##dictpiglatin = dict()
####Use {} curly brackets to construct the dictionary, and [] square brackets to index it. 
##for word in sentencetotranslate.split(' '):
####add a space after each word
##    piglatinword = main.translate(word)
##    if piglatinword in dictpiglatin: ##if it exisits
##        dictpiglatin[piglatinword] += 1
##    else:
##        dictpiglatin[piglatinword] = 1
##    piglatinsentence += piglatinword + ' '
##       
#print(piglatinsentence)

#print("frequency analysis")
        #for key in dictpiglatin:
        #   print("key -> value  =   -->  ", key, dictpiglatin[key])
        #Not Accessible 


        #print("translated sentence")
        ##for key in dictpiglatin:
          #  piglatinsentence += key + ' '

        #print(piglatinsentence)

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


def frame(root, side):
    w = Frame(root)
    w.pack(side = side, expand = YES, fill = BOTH)
    return w


class GUIOutput(Frame):
    #def __init__(self, frame): - when frame is a member variable
    def __init__(self):
        #inherited from frame
        Frame.__init__(self)

        #Funny error - Recursion
        #super(GUIOutput, self.__init__())

        
        
        
        self.pack(expand =  YES, fill = BOTH)
        self.master.title('Piglatin Generator')
        #can set the icon name too, here

        #parameter is the frame and we assign it as a class member variable
        #self.frame = frame 
        #frame.title("PigLatin Translator")

        #self.label = Label(frame, justify=LEFT, padx=10, compound = LEFT, text="English Text")
        #self.label.pack()
        #self.label1 = Label(frame, text="Translated Text")
        #self.label1.pack()

##        self.text_sentencetotranslate = Text(frame, height = 2, width= 100)
##        self.text_sentencetotranslate.pack()
##
##        self.text_piglatinsentence = Text(frame, height = 2, width= 100)
##        self.text_piglatinsentence.pack()

        
        #reusing the quit call back provided by Tkinter
##        self.quit_button = Button(frame, text = "Quit",  command = frame.quit)
##        self.quit_button.pack()
##        
##        self.translate_button = Button(frame, text = "Translate", command = self.translate)
##        self.translate_button.pack()
        

        #engFrame = frame(self, LEFT) #not using the function anymore
        engFrame = Frame(self)
        engFrame.pack(fill = X)
        lengText = Label(engFrame, text="English Text")        
        lengText.pack(side=LEFT, padx=5, pady=5)
        
        
        varToTranslate =  StringVar()
        #text_sentencetotranslate = Entry(frame(self, LEFT), textvariable=varToTranslate) #Enter the translated text
        text_sentencetotranslate = Entry(engFrame, textvariable=varToTranslate) #Enter the translated text
        text_sentencetotranslate.pack(fill=X, padx=5, expand=True)
        
        piglatinFrame = Frame(self)
        piglatinFrame.pack(fill = X) #else take it in the old frame's place and not visible
        #w1 = Label(frame(self, LEFT), text="Translated Text")
        lpiglatinText = Label(piglatinFrame, text="Translated Text")
        lpiglatinText.pack(side=LEFT, padx=5, pady=5)


        varTranslated =  StringVar()
        #text_piglatinsentence = Entry(frame(self, LEFT), textvariable=varTranslated)
        text_piglatinsentence = Entry(piglatinFrame, textvariable=varTranslated)
        text_piglatinsentence.pack(fill=X, padx=5, expand=True)
        
        quitpiglatin = Button(frame(self, LEFT), text = "Quit",  command = self.master.quit)
        #function pointer
        translate = Button(frame(self, LEFT), text = "Translate", command = lambda: self.translate(varToTranslate, varTranslated))
        quitpiglatin.pack()
        translate.pack()

       # varTranslated.set('')
        

        
    def translate(self, sentencetotranslate, piglatinsentence  ):
        #populate text box
        piglatinObject = Piglatin.PigLatinTranslate()
        #piglatinObject.piglatinTranslateSentence(self.text_sentencetotranslate.get(1.0, END)
        #self.text_piglatinsentence.set_text(piglatinObject.piglatinTranslateSentence(self.text_sentencetotranslate.get() ))
        
        #members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        #print(members)
        piglatinsentence.set(piglatinObject.piglatinTranslateSentence(sentencetotranslate.get()))
        #return piglatinsentence

    


##def translateCallBack():
##    #populate text box
##    T.insert(END, sentencetotranslate)
##    T1.insert(END, piglatinsentence)
##
##def quitCallBack():
##    frame.quit()
##    frame.destroy()
    


#frame = tkinter.Tk()
##frame = Tk()
##piglatinGUI = GUIOutput(frame)
##frame.mainloop()




