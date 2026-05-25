n=[23,3,-23,8,-7,20,-32,8,16]
psum=[0 for i in range(len(n))]
psum[0]=n[0]
for i in range(1,len(n)):
    psum[i]=max(psum[i-1]+n[i],n[i])
print(psum)
print(max(psum))