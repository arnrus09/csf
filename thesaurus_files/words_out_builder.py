import os
#import shelve
import re

handleThesaurus = open(os.path.expanduser('~/Desktop/soule_thesaurus.txt'))
handleKeys = open(os.path.expanduser('~/keyDest.txt'))
readThesaurus = handleThesaurus.readlines()
readKeys = handleKeys.readlines()
            
verbA='_v. a._'
verbN='_v. n._'
adj='_a._'
adv='_ad.-'
noun='_n._'
conj='_conj._'
wordTypes=[verbA,verbN,adj,adv,noun,conj]

#thes = shelve.open('thes.dat',writeback=True)
out = open('worsd_out.txt','w')

numbers=['1','2','3','4','5','6','7','8']

for line in readThesaurus[81:80336]:
    if not line.isspace():
        if line[0]=='~' and line[1] in numbers:
            out.write('\r\n\t'+line)
        elif line[0]=='~':
            out.write('\r\n'+line)
        else:
            out.write('\r\n\t\t'+line)

