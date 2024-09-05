n=input().split(' ')
a=[]
for i in range(0,len(n)):
    if n[i] not in a:
        a.append(n[i])
print(*a)