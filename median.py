a=[10,20,30,40,50,60,70]
i=0
j=len(a)-1
while i<j:
    i+=1
    j-=1
median=(a[i]+a[j])//2
print(median)