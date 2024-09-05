n=input().split(",")
c=[]
for i in n:
    if i not in c:
        c.append(i)
c.sort()
d=','.join(c)
print(d)