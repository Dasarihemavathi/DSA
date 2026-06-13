a=[1,2,2,4,4,5,8,1,9]
# find the duplicates in an array
visited=set()# this is set hashmap

result=[]
for i in a:
    if i in visited:
        result.append(i)
    else:
        visited.add(i)
        
print(result)
