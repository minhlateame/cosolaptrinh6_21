x=int(input())
n=int(input())
L=[]
for i in range(n):
    a=int(input())                             
    L=L+[a]
def Search(L,x):
    i=0
    k=0
    for i in range (len(L)):
        if x!=L[i]:
            k=k+1
        else:
            break
    return k
a=Search(L,x)
if a==len(L):
    print(None)
else:
    print(a)                 