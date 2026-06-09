s1=input()
s2=input()
a=list(s1)
b=list(s2)
ans="True"
if len(a)!=len(b):
    ans="False"
    
else:
    for i in range(0,len(a)-1+1,1):
        if a[i]!=b[i]:
            ans="false"
            
print(ans)
            

            
    