n=input()
a=n.split(',')
l=[]
for i in range (0,len(a)):
    if int(a[i],2)%3==0:
        l=l+[a[i]]
c=','.join(l)
print(c)