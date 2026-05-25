
def fact(n):
    ans=1
   
    for i in range(1,n+1,1):
        ans=ans*i
    return ans
n=10

fact(n)
r=2
npr=fact(n)/fact(n-r)
ncr=fact(n)/(fact(r)*fact(n-r))
print(ncr)
print(npr)
