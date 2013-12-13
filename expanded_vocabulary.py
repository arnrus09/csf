
import shelve
import random

def findEnd(string):
    index=0
    for c in string:
        if not c.isalpha():
            return index
        index+=1
    return -1

def removeUnicde(phrase):
    out=''
    for w in phrase:
        try:
            out+=str(w)
        except UnicodeEncodeError:
            continue
    return out
    
def sample(words):
    return random.choice(words)
    
def suffixify(suffix,word):
    return word+suffix
    
def shorten(word,suffix):
    return word[:-len(suffix)]
    
def endsWith(word,suffix):
    return word[-len(suffix):]==suffix
   
def suffixifyLists(suffix, superList):
    out=[]
    for t in superList:
        temp=[]
        temp=[suffixify(suffix,x) for x in t if not endsWith(x,'e')]
        if len(temp)!=len(t):
            for w in t:
                if endsWith(x,'e'):
                    temp.append(suffixify(suffix,shorten(w,'e')))
        out.append(temp)
    return out  
    
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
        self.searchWord=self.string.lower().capitalize()
        self.categories=[]
        for key in thesaurus:
            if self.searchWord==key:
                self.categories=thesaurus[key][:]
        self.Query('ing',thesaurus)
        self.Query('s',thesaurus)
        self.Query('ed',thesaurus)
    def Query(self,suffix,thesaurus):
        if endsWith(self.searchWord,suffix):
            for key in thesaurus:
                if shorten(self.searchWord,suffix)==key:
                    self.categories.extend(suffixifyLists(suffix,thesaurus[key][:])) 
                if shorten(self.searchWord,suffix)==shorten(key,'e') and endsWith(key,'e'):
                    self.categories.extend(suffixifyLists(suffix,thesaurus[key][:]))
    def hasSynonyms(self):
        return len(self.categories)!=1
    def initCategory(self):
            self.category=self.categories[0]
    def buffet(self):
        self.reference={'0':[str(self)]}
        self.question='\"'+str(self)+'\"'+sample([' like',' as in'])+':\r\n'
        intdex=0
        for c in self.categories:
            intdex+=1
            strdex=str(intdex)
            taste=sample(c) 
            self.reference[strdex]=c
            self.question+=strdex+'. '+'\"'+taste+'\"'+'\r\n'
        self.refLength=str(intdex+1)
        self.question+='0'+'. '+'leave as is\r\n\r\n'
    def ask(self):
        answer=(str(raw_input(self.question)))
        try:
            self.category=self.reference[answer]
        except:
            clarifiers=['that is not an option','beg your pardon?','I don\'t understand you','you may enter a number between 1 and %s'%(self.refLength)]
            retry=str(raw_input(sample(clarifiers)+'\r\n\r\n'))
            while retry not in self.reference:
                retry=str(raw_input(sample(clarifiers)+'\r\n\r\n'))
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
            if not phrase[index-1].isalpha():
                start=index
            while (phrase[index+1].isalpha() or phrase[index]=='\'') and index<test-1:
                index+=1
                word.cat(phrase[index])
            word.getEquivilants(thesaurus)
            if word.categories:
                if word.hasSynonyms():
                    try:
                        bndry1=phrase[:start].rindex('.')+1
                    except:
                        bndry1=0
                    try: 
                        bndry2=phrase[start:].index('.')+start
                    except:
                        try:
                            bndry2=phrase[start:].index('?')+start
                        except:
                            try:
                                bndry2=phrase[start:].index('!')+start
                            except:
                                bndry2=-1
                    if bndry2==-1 or bndry2-start>40:
                        try:
                            if phrase[start:].index(',')+start<bndry2:
                                bndry2=phrase[start:].index(',')+start
                            else:
                                pass
                        except:
                            pass  
                    wordEnd=findEnd(phrase[start:])+start
                    prt1=phrase[bndry1:start]
                    hiLightW=phrase[start:wordEnd].upper()
                    prt2=phrase[wordEnd:bndry2]
                    sentence='\r\n'+prt1+hiLightW+prt2
                    word.buffet()
                    print sentence
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
    
header='--this program helps you be more expressive\r\nby converting your words, it has learned most of what it knows from\r\n\"A Dictionary of English Synonymes and Synonymous or Parallel Expressions\r\nDesigned as a Practical Guide to Aptness and Variety of Phraseology\" by Richard Soule.\r\nEnter how many conversions you want and the content you wish to have translated.\r\nIf the meaning of a given word is ambiguous, you will be asked to clarify.\r\nSelect the number of the proper equivelant or 0 if none are suitable.\r\nA slice of the entry around the word will appear to remind you\r\nof what you meant in a given instance\r\n--'
    
def main():
    print header
    wordsIn=shelve.open('soule___reference.dat',writeback=True)
    scold=['I asked for a number','excuse me, type a number','That is not a valid entry']
    try:
        conversions=int(raw_input('how many phrases do you want converted?\r\n'))
    except:
        conversions=str(raw_input(sample(scold)+'\r\n'))
        while not conversions.isdigit():
            conversions=str(raw_input(sample(scold)+'\r\n'))
        conversions=int(conversions)
    for i in range(conversions):
        phrase=removeUnicde(raw_input('\r\nwhat would you like converted?\r\n'))
        convert(phrase,wordsIn)                              
    wordsIn.close() 
    
main()  