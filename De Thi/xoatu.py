n=input().split(' ')
c=[]
for i in range(0,len(n)):
    if i!=4 and i!=1 and i!=3:
        c.append(n[i])
print(c)