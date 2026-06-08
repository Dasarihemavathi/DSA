v=['a','e','i','o','u','A','E','I','O','U']
a="pavan prakash"
b=list(a)
a=""
count=0
for i in b:
    if i in v:
        count+=1
    else:
        a+=i 
print(a)