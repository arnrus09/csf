import os

handleThesaurus = open(os.path.expanduser('~/Desktop/soule_thesaurus.txt'))
readThesaurus = handleThesaurus.readlines()

keyWords = {}


letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

def letterTest(w):
    for c in w:
        if c in letters:
            return True
    return False

        

for i in readThesaurus:
    if '~, _v. ' in i:
        if ']' in i:
            keyWords[i[1:i.index(',')-1]] = i[i.rindex(']')+1:].split(',')
        elif '1' in i:
            keyWords[i[1:i.index(',')-1]] = i[i.rindex('~')+1:].split(',')
        elif '~, _v. a._' in i:
            try:
                keyWords[i[1:i.index(',')-1]] = i[i.rindex('a._')+3:].split(',')
            except:
                keyWords[i[1:i.index(',')-1]] = []
        elif ', _v. n._':
            try:
                keyWords[i[1:i.index(',')-1]] = i[i.rindex('n._')+3:].split(',')
            except:
                keyWords[i[1:i.index(',')-1]] = []
        dex = 1
        while '~,' not in readThesaurus[readThesaurus.index(i)+dex] and 'Cambridge: Press of John Wilson and Son.' not in readThesaurus[readThesaurus.index(i)+dex]:
            j = readThesaurus[readThesaurus.index(i)+dex]
            if '.~' in j:
                for p in j[j.rindex('.~')+2:].split(','):
                    keyWords[i[1:i.index(',')-1]].append(p)
            else:
                for s in j.split(','):
                    keyWords[i[1:i.index(',')-1]].append(s)
            dex += 1
        temp = []
        for w in keyWords[i[1:i.index(',')-1]]:
            if '_' not in w and '(' not in w and ')' not in w and letterTest(w) == True and w[-2:] == '\r\n':
                temp.append(w.strip().lower()+' ')
            if '_' not in w and '(' not in w and ')' not in w and letterTest(w) == True:
                temp.append(w.strip().lower())
        tempString = ''
        for x in temp:
            if ' ' in x:
                pass
            elif len(x) <= 2:
                pass
            elif temp[temp.index(x)-1][-1] == ' ' and temp[temp.index(x)-1][-2] != ',':
                pass
            elif x[-1] == '.':
                tempString += x[:-1]+',' 
            elif x[-1] == ' ' and (x[-2] == ',' or x[-2] == '.'):
                tempString += x[:-2]+','
            elif x[-1] == ',':
                tempString += x
            else:
                tempString += x+','
        keyWords[i[1:i.index(',')-1]] = tempString
        if letterTest(keyWords[i[1:i.index(',')-1]]) == False:
            del keyWords[i[1:i.index(',')-1]]


outToFile = open('soule_verb_modified.txt','w')

for key in keyWords:
    outToFile.write('\n'+' '+key.upper()+' '+'\n'+keyWords[key]+'\r\n')
outToFile.close()



