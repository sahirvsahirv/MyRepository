import unittest

from Piglatin import *

class PiglatinTest(unittest.TestCase):
    def test_translate_sentence(self):
        translate = PigLatinTranslate()
        translatedtext = translate.piglatinTranslateSentence("I am a girl")
        #print(translatedtext)
        #for letter in translatedtext:
         #   print(letter)
        self.assertTrue("I amway away irlgay " == translatedtext)

if __name__ == '__main__':
    unittest.main()
    
