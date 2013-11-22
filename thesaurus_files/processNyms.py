import os
handleThesaurus = open(os.path.expanduser('~/Desktop/synonymsEdited.txt'))
readThesaurus = handleThesaurus.readlines()
word = 'abash'
breaks = []
dex = 0


#while dex < len(readThesaurus):  #word.upper()+'.'+'\n' in line:  
#    if '*       *       *       *       *' in readThesaurus[dex]:
#        breaks.append(dex)
#    dex += 1 
for line in readThesaurus:
    if '_'+word.lower()+'_'  not in line and '_'+word.lower()+'d'+'_' not in line and '_'+word.lower()+'ed'+'_' not in line and '_'+word.lower()+'s'+'_' not in line:
        print line

#breaks.sort()
#print breaks