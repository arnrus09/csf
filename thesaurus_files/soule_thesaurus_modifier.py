import os

handleThesaurus = open(os.path.expanduser('~/Desktop/soule_thesaurus.txt'))
readThesaurus = handleThesaurus.readlines()

keyWords = []

symbols = '~ _()'
letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-\' '

for i in readThesaurus:
    if '~, _' in i:
        keyWords.append(i[1:i.index(',')-1])
keyWords = set(keyWords)
keyWords = list(keyWords)



def getVerbs():                
    verbs = {}        
    for k in keyWords:
        for ln in readThesaurus[:4000]:
            if '~'+k+'~, _v. n._' in ln:
                verbs[k] = ''
                temps = []
                dex = readThesaurus.index(ln)
                for wd in readThesaurus[dex].split(','):
                    temps.append(wd.strip())
                dex += 1
                while '_ad._' not in readThesaurus[dex] and '_v. a._' not in readThesaurus[dex] and '_n._' not in readThesaurus[dex] and '_a._' not in readThesaurus[dex] and '_prep._' not in readThesaurus[dex]:
                    print readThesaurus[dex]
                    temps = []
                    tempStr = ''
                    for word in readThesaurus[dex].split(','):
                        if '~' not in word and '_' not in word and '(' not in word and ')' not in word and '\"' not in word:
                            print word
                            temps.append(word.strip())
                    print temps
                    for wrd in temps:
                        if ' ' not in word and word != '':
                            outWord = ''
                            for c in wrd:
                                if c in letters:
                                    outWord += c
                            verbs[k] += outWord.lower()+', '
                    dex += 1
                    print '###', verbs[k]
    return verbs
    
verbs = getVerbs()
#for m in verbs:
#    print m+'\r\n'+verbs[m]


#writeVerbs = open('soule_verbsC.txt','w')



    
for m in verbs:
    if verbs[m] != '' and ', ,' not in verbs[m]:
        print '!!!', '\n'+m+'.'+'\n'+verbs[m]+'\r\n'
#        writeVerbs.write('\n'+m+'.'+'\n'+verbs[m]+'\r\n')