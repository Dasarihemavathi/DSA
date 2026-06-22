n=int(input("e"))
temp=n 
sum=0
l=len(str(n))
# if n<0:
#     print("naa")
    
while temp>0:
    temp=temp%10
    sum+=temp**(l)
    temp=temp//10
    
if sum==n:
    
    print("an")
    
else:
    print("nan")