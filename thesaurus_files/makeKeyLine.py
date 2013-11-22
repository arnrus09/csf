import os

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

letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

def letterTest(w):
    for c in w:
        if c in letters:
            return True
    return False

def getKeys(fh):
    keys = []
    for line in fh:
        if line == line.upper() and letterTest(line):
            keys.append(line[:-2]+'*')
    return keys

def keyWrite(fl,name):
    keyDest = open('keyDest.txt', 'a')
    keyDest.write('\r\n\r\n\r\n'*20+name.upper()+':\r\n\r\n\r\n'*20+str(getKeys(fl)))


keyWrite(verbs,'verbs')
keyWrite(advs,'advs')
keyWrite(adjs,'adjs')
keyWrite(conjs,'conjs')