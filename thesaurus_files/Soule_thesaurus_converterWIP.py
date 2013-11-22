"""excepts a specified amount of phrases from user and returns phrases of aproximately equivelant meanings"""
import random
import os

handleThesaurus = open(os.path.expanduser('~/soule_noun_updated.txt'))
readThesaurus = handleThesaurus.readlines()

numConversions = int(raw_input('number of phrases to covert: '))


punctuation = r',./;[]\-=<>?:"{}|_+`~!@#$%^&*()'
letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM\''

def convertWord(word):
    nyms = []
    for line in readThesaurus:
        if ' '+word.upper()+' ' in line:
            for w in readThesaurus[readThesaurus.index(line)+1].split(','):
                if w != '\r\n':
                    nyms.append(w)
            return random.choice(nyms)
    return word
        
    
                    
            
def convertPhrase(phrase):
    out = ''
    for word in phrase.split():
        textWord = ''
        for c in word:
            if c not in punctuation:
                textWord += c
        new = word.replace(textWord, convertWord(textWord))
        out += new+' '
    print out
        
for i in range(numConversions):
    rawPhrase = raw_input('phrase to covert: ')
    phrase = str(rawPhrase)
    convertPhrase(phrase)

