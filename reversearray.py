a=input("enter input :")
b=list(a)
i=0
j=len(a)-1
while i<j:
    b[i],b[j]=b[j],b[i]
    i=+1
    j=-1
a=" "
for i in b:
    a=a+i 
print(a)