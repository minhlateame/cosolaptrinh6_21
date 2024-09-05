n=input().split(' ')
s=[]
c=[]
for i in range(0,len(n)):
    if n[i].isnumeric()==True:
        s=s+[n[i]]
min=min(s)
max=max(s)
c=[int(max),int(min)]
print(c)    