a=[10,20,30,40,50,60,70,80,90,100]
i=0
j=len(a)-1
x=90
ans="not found"
while i<=j:
    mid=(i+j)//2
    if x==a[mid]:
        ans="found"
        break
    elif x>a[mid]:
        i=mid+1
    else :
        j=mid-1
        
print(ans)

