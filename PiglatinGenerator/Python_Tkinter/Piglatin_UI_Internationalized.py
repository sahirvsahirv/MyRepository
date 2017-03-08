import Piglatin

import os
import locale

#Returns unicode string automatically in Python 3
#from gettext import gettext as _
import gettext

#Ideally you have VM's for each locale and connect remotely to those machines to
#test the code
import config

#print(_('hello'))
#print(_('how are you?'))


locale_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale\\')
current_locale, encoding = locale.getdefaultlocale()
print(locale_dir)
#gettext.install(domain, localedir=None, codeset=None, names=None)

#File names and log files will never be localized
#gettext.textdomain('Piglatin_UI_Internationalized')
# Set up message catalog access

#translation file as the first parameter , mo file -GNU
#gettext.bindtextdomain('hi', locale_dir)
#gettext.textdomain('hi')
#_ = gettext.gettext

#print(_('hello'))
#print(_('how are you?'))

os.environ.setdefault('LANG', 'af')

#class based api
#t = gettext.find('hi', locale=locale_dir)
t = gettext.translation('Piglatin_UI_Internationalized', locale_dir)
t.install()
_ = t.gettext


class ConsoleOutput:
    def __init__(self):
        ##analyze frequencies
        piglatinObject = Piglatin.PigLatinTranslate()
        #print(__name__)
        if __name__ == "__main__":
            #print("from commandline")
            piglatinObject.piglatinTranslate(_("hello"))
            print(_("testing with hello == "), piglatintext)

            print(_("sentence translation"))
            piglatinObject.piglatinTranslateSentence(_("i am gowri and you are you"))

            print(_("frequency analysis"))
            print("%s" %(piglatinObject.frquencyAnalysis()))
        elif __name__ == "Piglatin_UI":
            #print("from module - testingPiglatin_commandline being the name of the module in this case")

            #Internationalization
            t = gettext.translation('English', '/locale')
            _ = t.ugettext
            
            texttotranslate = input(_("Enter text - a word: "))
            print("translated = ", piglatinObject.piglatinTranslate(texttotranslate))
            
            sentencetotranslate = input(_("Enter text - a sentence: "))
            print(_("translated text = "), piglatinObject.piglatinTranslateSentence(sentencetotranslate))

            print(_("frequency analysis"))
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

        
        
        self.master.title(_('Piglatin Generator'))

        #If you want to make the widgets as wide as the parent widget, you have to use the fill=X option: 
        lengText = Label(self.master, text=_('English Text'))
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
        
        
        translate = Button(self.master, text = _("Translate"), command = lambda: self.translate(varToTranslate, varTranslated))
        translate.grid(row=2, columnspan= 2, sticky = E)

        #Disable it so that the text cannot be changed
        text_piglatinsentence.config(state=DISABLED)
        
        quitpiglatin = Button(self.master, text = _("Quit"),  command = self.quitCallBack)
        quitpiglatin.grid(row=2, column=4, columnspan=4,  sticky = E)
        #function pointer
        
        
    def translate(self, sentencetotranslate, piglatinsentence  ):
        #populate text box
        piglatinObject = Piglatin.PigLatinTranslate()
        piglatinsentence.set(piglatinObject.piglatinTranslateSentence(sentencetotranslate.get()))
        
        

    def quitCallBack(self):
        self.master.quit()
        self.master.destroy()




