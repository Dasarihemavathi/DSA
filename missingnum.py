n=8
a=[1,2,3,4,5,6]
sum1=0
for i in range(0,len(a)-1+1,1):
    sum1+=i
    
sum2=0
for i in a:
    sum2+=i
print(sum2-sum1)

