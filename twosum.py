a=[12,3,41,2,3,12,31,23,11]
sum=15
for i in range(0,len(a)-1+1,1):
    for j in range(i+1,len(a)-1+1,1):
        if a[i]+a[j]==sum:
            print(a[i]," ",a[j])
        
