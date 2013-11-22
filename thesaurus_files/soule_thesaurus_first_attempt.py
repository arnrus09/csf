import os
import random

#Bugs: commas seperating lines, different meanings


handleNoun = open(os.path.expanduser('~/soule_noun_modified.txt'))
handleVerb = open(os.path.expanduser('~/soule_verb_modified.txt'))
handleAdj = open(os.path.expanduser('~/soule_adj_modified.txt'))
handleAdv = open(os.path.expanduser('~/soule_adv_modified.txt'))
handleConj = open(os.path.expanduser('~/soule_conj_modified.txt'))
nouns = handleNoun.readlines()
verbs = handleVerb.readlines()
adjs = handleAdj.readlines()
advs = handleAdv.readlines()
conjs = handleConj.readlines()

wordTypeList = [nouns, verbs, adjs, advs, conjs]

punctuation = r',./;[]\-=<>?:"{}|_+`~!@#$%^&*()'

def routeWord(word):
    possibleTypes = []
    for t in wordTypeList:
        if ' '+word.upper()+'*' in t[1]:
            possibleTypes.append(t)
    return possibleTypes
        
def convertWord(word):
    dests = routeWord(word)
    nyms = []
    loc = []
    if len(dests)==0:
        return word
    elif len(dests)==1:
        loc=dests[0]
    else:
        print '\r\n'+word.upper()
        route = str(raw_input('in which part of speach?\r\n'))
        for t in dests:
            if route.upper() in t[0]:
                loc = t
        if loc == []:        
            print 'thats not right!'
            return convertWord(word)
    for line in loc:
        if ' '+word.upper()+' ' in line:
            for w in loc[loc.index(line)+1].split(','):
                nyms.append(w)
            break
    return random.choice(nyms)                        
    

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
    
def main():  
    numConversions = int(raw_input('number of phrases to covert: '))   
    for i in range(numConversions):
        rawPhrase = raw_input('phrase to covert: ')
        phrase = str(rawPhrase)
        convertPhrase(phrase)

#main()