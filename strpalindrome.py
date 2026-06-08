a=input("enter any string :")
b=list(a)
ans= "True"
i=0
j=len(a)-1
while i<j:
    
    if b[i]!=b[j]:
        ans= "False"
        break
    i+=1
    j-=1
        
print(ans)