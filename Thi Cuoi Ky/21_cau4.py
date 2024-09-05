n=input().split(' ')
l=[]
for i in range(len(n)):
    if n[i]=='Python':
        l=l+['Java']
    elif n[i]=='Java':
        l=l+['Python']
    else:
         l=l+[n[i]]
print(*l)
        
