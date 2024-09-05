x=str(input())
k=int(input( ))
n=int(input())
L=[]
for i in range(n):
    a=int(input())                             
    L=L+[a]
def add(L,x,k):
    if k>len(L):
        L=L+[x]
    else:
        L=L[:k-1]+[x]+L[k-1:]
    return(L)
a=add(L,x,k)
print(a)        