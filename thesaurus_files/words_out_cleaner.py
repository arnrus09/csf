import os
#import shelve


handleThesaurus = open(os.path.expanduser('~/worsd_out_d.txt'))

readThesaurus = handleThesaurus.readlines()

            
verbA='_v. a._'
verbN='_v. n._'
adj='_a._'
adv='_ad._'
noun='_n._'
conj='_conj._'
wordTypes=[verbA,verbN,adj,adv,noun,conj]

#thes = shelve.open('thes.dat',writeback=True)
out = open('worsd_out_e.txt','w')

numbers=['1','2','3','4','5','6','7','8']


testD = {}

"""for line in readThesaurus:
    if line[0]=='~':
        for t in wordTypes:
            if t in line:
                word = line[:line.index(',')]+t
                break
            else:
                pass
        testD[word]={}"""
outlist=[]        
        
for line in readThesaurus:
        if '(' in line or ')' in line:
            lin = line
            if '(' in line and ')' in line:
                while '(' in lin and ')' in lin:
                    if lin.rindex(')')>lin.index('('):
                        lin=lin[:lin.index('(')]+lin[lin.rindex(')')+1:]
                    elif lin.index('(')>lin.rindex(')'):
                        lin=lin[lin.index('(')+1:]+lin[:lin.rindex(')')]
            if '(' in lin:
                while '(' in lin:
                    lin=lin[:lin.index('(')]
            if ')' in lin:
                while ')' in lin:
                    lin=lin[lin.rindex(')')+1:]
            outlist.append(lin)
        else:
            outlist.append(line)

out.writelines(outlist)

    
