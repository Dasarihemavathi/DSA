a=[1,3,30,0,24,0,0,0,2,32,2,0,0,2]
j=0
for i in a:
    if i!=0:
        a[j]=i 
        j=j+1
        
while j<=len(a)-1:
    a[j]=0
    j+=1
    
print(a)
