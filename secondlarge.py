def secondlargest(lst):
    first=float('-inf')
    second=float('-inf')
    for num in lst:
        if num>first:
            second=first 
            first=num 
        elif num>second and num!=first:
            second=num 
    print(second)
    
lst=list(map(int,input().split()))    
secondlargest(lst)
