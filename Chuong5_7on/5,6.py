a=[]
for i in range(0,10,1):
    x=input()
    a=a+[x]
b=a.copy()
for i in range(0,6,2):
    b[i]=a[i+1]
    b[i+1]=a[i]
print(*b)