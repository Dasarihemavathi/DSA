a="pavan prakash Dhee Coding Lab"
cap=0
small=0
dig=0
spaces=0
spc=0
word=0
b=list(a)
for i in b:
    if i>='A' and i<='Z':
        cap=cap+1
    elif i>='a' and i<='z':
        small=small+1
    elif i>='0' and i<='9':
        dig=dig+1
    elif i==' ':
        spaces=spaces+1
    else:
        spc=spc+1
        
word=spaces+1
print(word)
print(cap)
print(small)
print(dig)
print(spaces)
print(spc)