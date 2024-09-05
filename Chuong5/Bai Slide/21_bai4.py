n=int(input())
L=[]
for i in range(n):
    a=int(input())                             
    L=L+[a]
def count(L):
    k=0
    for i in range (len(L)):
        k=k+1
    return(k)
k=count(L)
print(k)