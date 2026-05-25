nums=list(map(int,input("enter the elements here :").split()))

for i in range(0,len(nums)-1+1,1):
    for j in range(i+1,len(nums)-1+1,1):
        if nums[i]>nums[j]:
            nums[i],nums[j]=nums[j],nums[i]

print("the sorted elements are :",nums)