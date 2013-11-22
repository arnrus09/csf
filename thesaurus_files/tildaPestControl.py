import os

handleThesaurus = open(os.path.expanduser('~/Desktop/soule_thesaurus.txt'))
readThesaurus = handleThesaurus.readlines()

def illegalTilda(c, line):
    for i in '1234567890':
        if line[line.index(c)+1] == i or line[line.index(c)-2] == i:
            return False
        return True
            


for i in readThesaurus:
    if '~' in i:
        if illegalTilda and i[0]!='~':
            print i, readThesaurus[readThesaurus.index(i)-1], readThesaurus[readThesaurus.index(i)+1]
