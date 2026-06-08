a="my name is pavanprakash539"
b=list(a)
for i in range(0,len(b)-1+1,1):
    for j in range(i+1,len(b)-1+1,1):
        if a[i]<a[j]:
            b[i],b[j]=b[j],b[i]
        
a=""
for i in b:
    a+=i 
print(a)