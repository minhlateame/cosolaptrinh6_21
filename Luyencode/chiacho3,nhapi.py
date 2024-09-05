i,n=map(int,input('').split())
s=0
#for i in range(i+1,n): 
for n in range (n-1,i,-1):
    if n%3==0:
        print(n,end=" ")
        s=s+n
if s==0:
    print('NOT FOUND')