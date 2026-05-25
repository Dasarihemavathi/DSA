n=[12,9,3,5,2,5,2,3,22,6,22,45]
psum=[0 for i in range(len(n))]
psum[0]=n[0]
for i in range(1,len(n)-1+1):
    psum[i]=psum[i-1]+n[i]
print(psum)
    
