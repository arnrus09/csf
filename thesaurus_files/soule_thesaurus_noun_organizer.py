import os

handleThesaurus = open(os.path.expanduser('~/Desktop/soule_thesaurus.txt'))
readThesaurus = handleThesaurus.readlines()

keyWords = {}


letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '1234567890'

def letterTest(w):
    for c in w:
        if c in letters:
            return True
    return False

        

for i in readThesaurus:
    if '~, _n._ ' in i:
        if ']' in i:
            keyWords[i[1:i.index(',')-1]] = i[i.rindex(']')+1:]
            try:
                keyWords[i[1:i.index(',')-1]] = keyWords[i[1:i.index(',')-1]][keyWords[i[1:i.index(',')-1]].rindex('~')+1:].split()
            except:
                keyWords[i[1:i.index(',')-1]] = keyWords[i[1:i.index(',')-1]].split()
        elif '1' in i:
            keyWords[i[1:i.index(',')-1]] = i[i.rindex('~')+1:].split(',')
        else:
            keyWords[i[1:i.index(',')-1]] = i[i.rindex('_n._')+4:].split(',')
        dex = 1
        while '~,' not in readThesaurus[readThesaurus.index(i)+dex] and 'Cambridge: Press of John Wilson and Son.' not in readThesaurus[readThesaurus.index(i)+dex]:
            if readThesaurus[readThesaurus.index(i)+dex][0] == '~' and readThesaurus[readThesaurus.index(i)+dex][1] not in numbers:
                pass
            else:
                j = readThesaurus[readThesaurus.index(i)+dex]
                if ']' in readThesaurus[readThesaurus.index(i)+dex]:
                    try:
                        for p in j[j.rindex(']')+1:].split(','):
                            keyWords[i[1:i.index(',')-1]].append(p) 
                    except:
                        continue
                if '.~' in j and j[1] in numbers:
                    for p in j[j.rindex('.~')+2:].split(','):
                        keyWords[i[1:i.index(',')-1]].append(p)
                else:
                    for s in j.split(','):
                        keyWords[i[1:i.index(',')-1]].append(s)
            dex += 1
        temp = []
        for w in keyWords[i[1:i.index(',')-1]]:
            if '_' not in w and letterTest(w) == True and w[-2:] == '\r\n':
                temp.append(w.strip().lower()+' ')
            elif '_' not in w and letterTest(w) == True:
                temp.append(w.strip().lower())
        tempString = ''
        for x in temp:
            if len(x) <= 4 and not letterTest(x):
                pass
            elif x[-1] == '.':
                tempString += x[:-1]+',' 
            elif x[-1]==' ' and (x[-2] == ',' or x[-2] == '.'):
                tempString += x[:-2]+','
            elif x[-1]==' ' or x[-1] == ',':
                tempString += x
            else:
                tempString += x+','
        keyWords[i[1:i.index(',')-1]] = tempString
        if letterTest(keyWords[i[1:i.index(',')-1]]) == False:
            del keyWords[i[1:i.index(',')-1]]


outToFile = open('soule_noun_modified.txt','w')

for key in keyWords:
    outToFile.write('\n'+' '+key.upper()+' '+'\n'+keyWords[key]+'\r\n')
outToFile.close()



