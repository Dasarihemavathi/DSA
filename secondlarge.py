# # def secondlargest(lst):
# #     first=float('-inf')
# #     second=float('-inf')
# #     for num in lst:
# #         if num>first:
# #             second=first 
# #             first=num 
# #         elif num>second and num!=first:
# #             second=num 
# #     print(second)
    
# # lst=list(map(int,input().split()))    
# # secondlargest(lst)
# lst=[10,20,423,420,425,53,523,90,100]
# lst.sort()

# print(lst[-2])
def slarge(lst):
    large=float('-inf')
    slarge=float('-inf')
    for num in lst:
        if num>large:
            slarge=large
            large=num 
        elif num>slarge and num!=large:
            slarge=num
    print(slarge)
        
slarge([10,20,30,40,50,60])
            