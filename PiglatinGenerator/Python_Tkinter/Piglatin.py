class PigLatinTranslate:

    dictpiglatin = dict()
    
    #def __init__(self):
        ##vowels is a list

        ##This is a set
        ##vowels = ["a", "e", "i", "o", "u"] 

        ##frozen set
        ##vowels = frozenset(["a", "e", "i", "o", "u"])
        
        
        
        

    def piglatinTranslate(self, word):
        ##tuple - cant be changed
        vowels = "a", "e", "i", "o", "u"
        ##change all to lowercase
        #TODO:
        found = 0
        oldandleastindex = -1
        for i in vowels:
            index = word.find(i)
            #print(index)
            if(index != -1):
                found = 1
                if(index < oldandleastindex or oldandleastindex == -1):
                    oldandleastindex = index
                #else:
                    #do nothing 
        #for loop over
        #print(oldandleastindex)
        if(found == 1 and oldandleastindex != 0):
            return word[oldandleastindex:] + word[:oldandleastindex] + "ay"
        elif(found == 1 and oldandleastindex == 0):
            return word + "way"
        else:
            #print(word)
            return word ##no vowel - space quote etc
            

    def piglatinTranslateSentence(self, sentencetotranslate):
        piglatinsentence = ""
        
        ##Use {} curly brackets to construct the dictionary, and [] square brackets to index it. 
        for word in sentencetotranslate.split(' '):
            ##add a space after each word
            piglatinword = self.piglatinTranslate(word)
            if piglatinword in self.dictpiglatin: ##if it exisits
                self.dictpiglatin[piglatinword] += 1
            else:
                self.dictpiglatin[piglatinword] = 1
            #should happen for each word
            piglatinsentence += piglatinword + ' '
            ##TODO: Correct not to have space
        ##for loop over
        return piglatinsentence

    def frquencyAnalysis(self):
        immutable_tuple  =  tuple(sorted(self.dictpiglatin.items()))
        #dictionary implemented by hashing
        #tuples are slow
        return immutable_tuple


            

            
