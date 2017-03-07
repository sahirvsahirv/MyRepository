import Piglatin 


from tkinter import *

root = Tk()

piglatinFrame = Frame(root)
piglatinFrame.pack(expand =  YES, fill = BOTH)
#piglatinFrame.title('Piglatin Generator')

#Using the same frame all through out and the window expands horizontally
#piglatinFrame = Frame(self)
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

        
#defined earlier in the code
def translate():
    #populate text box
    piglatinObject = Piglatin.PigLatinTranslate()
    varTranslated.set(piglatinObject.piglatinTranslateSentence(varToTranslate.get()))


def quitCallBack():
    root.quit()
    root.destroy()



        
#function pointer
#Removing the neccessity of lambda function, by making the text boxes a member variable
translate = Button(piglatinFrame, text = "Translate", command = translate)
translate.pack(side=LEFT, padx=10)
#Disable it so that the text cannot be changed
text_piglatinsentence.config(state=DISABLED)

        
        
quitpiglatin = Button(piglatinFrame, text = "Quit",  command = quitCallBack)
quitpiglatin.pack(side=LEFT, padx=10)

root.mainloop()

        




