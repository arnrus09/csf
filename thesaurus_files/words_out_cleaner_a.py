import os
#import shelve


handleThesaurus = open(os.path.expanduser('~/worsd_out_e.txt'))

readThesaurus = handleThesaurus.readlines()

            
verbA='_v. a._'
verbN='_v. n._'
adj='_a._'
adv='_ad._'
noun='_n._'
conj='_conj._'
wordTypes=[verbA,verbN,adj,adv,noun,conj]

#thes = shelve.open('thes.dat',writeback=True)
#out = open('worsd_out_e.txt','w')

numbers=['1','2','3','4','5','6','7','8']


testD = {}

for line in readThesaurus[:100]:
    if line[0]=='~':
        word=line[:line.index('._')+2]
        testD[word]={}
        dex=1
        subLines=readThesaurus.index(line)
        testD[word]['usage']={}
        if '1.' in line:
            testD[word]['usage']['1']=line[line.rindex('_')+1:].strip()
        elif not line[line.rindex('_')+1:].isspace():
            testD[word]['usage']['only']=line[line.rindex('_')+1:].strip()
        while readThesaurus[subLines+dex][0]!='~':
            strippedLine=readThesaurus[subLines+dex].strip()
            if strippedLine[0]=='~':
                u=strippedLine[1:3]
                testD[word]['usage'][u]=strippedLine[strippedLine.rindex('~')+1:]
                dex+=1
            else:
                try:
                    testD[word]['usage'][u]=strippedLine
                except NameError:
                    try:
                        testD[word]['usage']['only']+=', '+strippedLine
                    except:
                        testD[word]['usage']['only']=strippedLine
                dex+=1
        try:
            del u
        except NameError:
            pass
#out.writelines(outlist)
print testD
    
