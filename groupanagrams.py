strs=['eat','cat','hat','act','cat','stop','tops','pots']
d={}
for word in strs:
    key="".join(sorted(word))
    print(key)
    
    if key not in d:
        d[key]=[]
    d[key].append(word)
print(list(d.values()))
