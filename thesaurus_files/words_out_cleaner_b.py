import os
import shelve


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
letters='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'

def letterTest(w):
    for c in w:
        if c in letters:
            return True
    return False
    
def convertLine(line,v):
    temp1=line.split(',')
    temp2=[]
    for w in temp1:
            if v and ' ' in w.strip():
                pass    
            elif w=='':
                pass
            elif '.' in w:
                temp2.append(w.replace('.',' ').strip().lower())
            elif w[-1]=='\n' and letterTest(w.lower()):
                try:
                    temp2.append(w[:-2].lower()+' ')
                except:
                    pass
            elif w.isspace():
                pass
            else:
                temp2.append(w.strip().lower())
    return temp2
    
    
def rejoin(l1,l2,hlt):
    if l1[-1][-1]==' ' and l2[0]!='' and not hlt:
        l1[-1]=l1[-1]+l2[0]
        l1.extend(l2[1:])
    else:
        l1.extend(l2)

testD = {}
for line in readThesaurus:
    if line[0]=='~':
        try:
            word=line[:line.index('._')+2]
            v=False
            if '_v.' in line:
                v=True
            testD[word]={}
            dex=1
            subLines=readThesaurus.index(line)
            testD[word]['usage']={}
            try:
                if not line[line.rindex('_')+1:].isspace():
                    testD[word]['usage']['0.']=convertLine(line[line.rindex('_')+1:],v)
            except:
                pass
            while readThesaurus[subLines+dex][0]!='~':
                thisLine=readThesaurus[subLines+dex]
                strippedLine=thisLine.strip()
                hlt=False
                if thisLine[0]==',':
                    hlt=True
                if strippedLine[0]=='~':
                    u=strippedLine[1:3]
                    testD[word]['usage'][u]=convertLine(thisLine[thisLine.rindex('~')+1:],v)
                    dex+=1
                elif testD[word]['usage'].get('0.'):
                    rejoin(testD[word]['usage']['0.'],convertLine(thisLine,v),hlt)
                    dex+=1
                else:   
                    try:
                        testD[word]['usage'][u]=rejoin(testD[word]['usage'][u],convertLine(thisLine,v),hlt)
                    except NameError:
                        testD[word]['usage']['0.']=convertLine(thisLine,v)
                    dex+=1
                try:
                    del u
                except NameError:
                    pass
        except:
            pass


sDB = shelve.open('souleDB.dat',writeback=True)
for i in testD:
    sDB[i]=testD[i]
for i in sDB:
    print i
sDB.close()
