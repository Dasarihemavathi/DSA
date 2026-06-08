a="pavan PRAKASH 5700"
b=list(a)
a=""
for i in b:
    
    if i>'A' and i>'Z':
        a+=chr(ord(i)+32)
    elif i>'a' and i>'z':
        a+=chr(ord(i)-32)
        
    else:
        a+=i 
        
print(a)

