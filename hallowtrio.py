n=int(input("enter number:"))
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if i==j or i+j==n+1 or i==1 or i==n or j==1 or j==n:
            print("H", end=" ")
        else:
            print(" ",end=" ")
    print()