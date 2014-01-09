bitStr=str(raw_input('bit string: '))
a=0
i=0
neg=False
lng=len(bitStr)
if lng<32:
    bitStr=(32-lng)*'0'+bitStr
elif lng>32:
    print 'Error: bit string is too large.'
if bitStr[0]=='1':
    neg=True
while i<32:
    if bitStr[31-i]=='1':
        a+=2**i
    i+=1
if neg:
    a=-(2**32-a)
print a