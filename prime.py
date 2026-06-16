# num=int(input())
# if num<2:
#     ans=False

# else:
#     ans=True
# # count=0
# for i in range(2,num,1):
#     if num%i==0:
#         ans=False
#         break
        
# print(ans)
#         # count+=1
# # if count==2:
# #     print("prime number")
# # else:
# #     print("not a prime number")
    
n1 = 1
n2 = 10

count = 0

for num in range(n1, n2 + 1):

    if num < 2:
        continue

    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        count += 1

print(count)

    
         
        