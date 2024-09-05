n=str(input()).split(',')
c=[]
a=[]
for i in n:
    if i not in c:
        c.append(i)
a=','.join(c)
print(a)
