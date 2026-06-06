a="Dhee"
b=list(a)
print(b)

b[0]="Z"
print(b)

a=""
for i in b:
    a+=i 
print("The original string is :",a)