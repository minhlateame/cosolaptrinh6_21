n=list(input())
a=[]
for i in n:
    if i.isalnum()==True:
        a.append(i)
print(*a,sep='')
        