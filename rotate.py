a=[10,20,30,40,50,60,70]
r=19
r=r % len(a)
for i in range(len(a)-r,len(a)-1+1,1):
    print(a[i]," ",end="") 
for i in range(0,len(a)-r-1+1,1):
    print(a[i]," ",end="") 
    

