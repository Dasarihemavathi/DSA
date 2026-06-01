a=[12,2,12,4,2,3,131,43,12,42,12]
i=0
j=len(a)-1
x=int(input("x:"))
ans="Found"
while i<=j:
    mid=(i+j)//2
    if x==a[mid]:
        ans="Found"
    elif x>a[mid]:
        i=mid+1
    else:
        j=mid-1
        
print(ans)
        
        
