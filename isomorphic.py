s="ekg"
t="egg"

h={}

for i in range(len(s)):
    if s[i] in h and h[s[i]]!=t[i]:
        print(False) 
    elif s[i] not in h and t[i] in h.values():
        print(False)
    else:
        h[s[i]]=t[i]
print(True)

