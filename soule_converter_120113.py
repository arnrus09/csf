
import shelve
import random

wordsIn=shelve.open('soule_reference.dat',writeback=True)
    
def sample(words):
    return random.choice(words)
    
class Characters(object):
    def __init__(self,character):
        self.string=character
        
    def cat(self,character):
        self.string+=character
    def __str__(self):
        return self.string
        
class Word(Characters):
    def __init__(self,character):
        Characters.__init__(self,character)
    def inThesaurus(self,thesaurus):
        self.searchWord=self.string.lower().capitalize()
        return self.searchWord in thesaurus
    def getEquivilants(self,thesaurus):
        for key in thesaurus:
            if self.searchWord==key:
                self.categories=thesaurus[key]
    def hasSynonyms(self):
        return len(self.categories)!=1
    def initCategory(self):
            self.category=self.categories[0]
    def buffet(self):
        self.reference={}
        self.question='\"'+self.__str__()+'\"'+sample([' like ',' as in '])
        for c in self.categories:
            taste=sample(c)
            self.reference[taste]=c
            self.question+='\"'+taste+'\"'+' or '
        self.question=self.question[:-4]+'?\r\n\r\n'
    def ask(self):
        try:
            self.category=self.reference[(str(raw_input(self.question)))]
        except:
            retry=str(raw_input(sample(['beg your pardon?','I don\'t know what you mean','I can only understand people who know how to spell'])+'\r\n\r\n'))
            while retry not in self.reference:
                retry=str(raw_input(sample(['beg your pardon?','I don\'t know what you mean','I can only understand people who know how to spell'])+'\r\n\r\n'))
            self.category=self.reference[retry]
    def finalAnswer(self):
        self.finalAnswer=sample(self.category)
        if str(self).istitle():
            return self.finalAnswer.capitalize()
        return self.finalAnswer
        
def convert(raw_phrase,thesaurus):
    phrase=raw_phrase+' '
    index=0
    finalAnswer=''
    test=len(phrase)
    while index<len(phrase)-1:
        if phrase[index].isalpha():
            word=Word(phrase[index])
            while (phrase[index+1].isalpha() or phrase[index]=='\'') and index<test-1:
                index+=1
                word.cat(phrase[index])
            if word.inThesaurus(thesaurus):
                word.getEquivilants(thesaurus)
                if word.hasSynonyms():
                    word.buffet()
                    word.ask()
                else:
                    word.initCategory()
                finalAnswer+=word.finalAnswer()
            else:
                finalAnswer+=str(word)
            del word
            if index<test-1:
                index+=1
        else:
            nonLetters=Characters(phrase[index])
            index+=1
            while not phrase[index].isalpha() and index<test-1:
                nonLetters.cat(phrase[index])
                if index<len(phrase)-1:
                    index+=1
            finalAnswer+=str(nonLetters)
            del nonLetters
        if not index<len(phrase):
            break
    print '\r\n\r\n'+finalAnswer+'\r\n\r\n'

conversions=int(raw_input('how many phrases do you want converted?\r\n'))
for i in range(conversions):
    phrase=str(raw_input('\r\nwhat would you like converted?\r\n'))
    convert(phrase,wordsIn)           
                   
wordsIn.close()   