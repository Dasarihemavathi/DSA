a=[12,3,23,1132,112,12,12,63,63,42]
# print(a)
# # selction sort is used to swap the elments in th list and also reverisgin an array indirectly
# for i in range(0,len(a)-1+1,1):
#     for j in range(i+1,len(a)-1+1,1):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)

i=0
j=len(a)-1
while i<=j:
    mid=(i+j)//2
    
    if a[i]>a[j]:
        
        
        a[i],a[j]=a[j],a[i]
        
    i+=1
    j-=1



    
    
    
