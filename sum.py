a=[10,20,30,40,40,503,230]  
p=[0]*len(a)
p[0]=a[0]
for i in range(1,len(a)-1+1,1):
    p[i]=p[i-1]+a[i]
print(p)
print(p[-1])

    
