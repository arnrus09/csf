import os
handleThesaurus = open(os.path.expanduser('~/synonyms2.txt'))
readThesaurus = handleThesaurus.readlines()
phrase = 'allege it\'s truth'
#phrase = raw_input('insert text to modify: ')
    
    
def findNyms(word):
    getNyms = []
    for i in readThesaurus:  #if word in thesaurus, returns synonyms
        if word in i:
            for j in readThesaurus[readThesaurus.index(i)+4:]:  #the syntax of thesaurus
                if '.' not in j:
                    for k in j.split():
                        getNyms.append(k)                
                else:
                    break
            nyms2 = getNyms[:]
            for l in getNyms: #merges two word synonyms
                if ',' not in l:
                    nyms2[getNyms.index(l)+1] = l+' '+ nyms2[getNyms.index(l)+1]
                    nyms2.remove(l)
            getNyms = []
            for m in nyms2:
                if ' ' not in m:#removes two word synonyms and commas
                    getNyms.append(m[:-1])
            return getNyms


for w in phrase.split():
    u = w.upper()+'.\n'  #words in thesaurus appear as: 'EXAMPLE.\n' on their own line.
    if u in readThesaurus:
        phrase = phrase.replace(w, findNyms(u)[(len(phrase)%len(findNyms(u)))]) #chooses random synonym
        
print phrase


                