n=input()
b=[]
a=0
for i in range(1,len(n)):
    if n[i]==':':
        a=1+i
b.append(n[a:])
print(*b)