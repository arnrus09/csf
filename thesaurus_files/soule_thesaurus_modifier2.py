import os

handleThesaurus = open(os.path.expanduser('~/Desktop/soule_thesaurus.txt'))
readThesaurus = handleThesaurus.readlines()

keyWords = {}

nums = '1.', '2.', '1.', '1.', '1.', '1.', '1.',
symbols = '~ _()'
letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

def letterTest(w):
    for c in w:
        if c in letters:
            return True
    return False
        

for i in readThesaurus:
    if '~, _n._ ' in i:
        if '1' in i:
            keyWords[i[1:i.index(',')-1]] = i[i.rindex('~')+1:].split(',')
        else:
            keyWords[i[1:i.index(',')-1]] = i[i.rindex('_n._')+4:].split(',')
        dex = 1
        while '~,' not in readThesaurus[readThesaurus.index(i)+dex]:
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
            if '_' not in w and letterTest(w) == True:
                temp.append(w.strip().lower())
        tempString = ''
        for x in temp:
            if x[-1] == ',' or x[-1] == '.':
                tempString += x[:-1]+','
            else:
                tempString += x+','
        keyWords[i[1:i.index(',')-1]] = tempString
        if keyWords[i[1:i.index(',')-1]] == '':
            del keyWords[i[1:i.index(',')-1]]

outToFile = open('soule_noun_file.txt','w')

for key in keyWords:
#    outToFile.write('\n'+' '+key.upper()+'\n'+keyWords[key]+'\r\n')
#outToFile.close()
    print key, keyWords[key]


