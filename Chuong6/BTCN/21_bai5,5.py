n=int(input('n='))
L=[]
for i in range (n):
    a=int(input())
    L=L+[a]
s=0
for i in range (0,n):
    if i%2!=0:
        s=s+L[i]
print('Tong=',s,sep="")