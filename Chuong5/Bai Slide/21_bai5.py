x=str(input())
y=str(input())
n=int(input())
L=[]
for i in range(n):
    a=int(input())                             
    L=L+[a]
def replace(L,x,y):
    i=0
    while i<(len(L)):
        if x==L[i]:
            L=L[:i]+[y]+L[i+1:]
        else:
            i=i+1
    return(L)
a=replace(L,x,y)
print(a)