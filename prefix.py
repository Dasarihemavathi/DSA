n=[23,3,42,23,24,24,6,8,16]
psum=[0 for i in range(len(n))]
psum[0]=n[0]
for i in range(1,len(n)):
    psum[i]=psum[i-1]+n[i]
print(psum)
    