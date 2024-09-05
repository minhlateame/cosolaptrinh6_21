n=int(input('n='))
i=0
l=[]
s=0
while i<n:
    x=str(input())
    l=l+[x]
    i=i+1
for i in range(1,len(l),2):
    s=s+int(l[i])
print('Tong=',s,sep='')