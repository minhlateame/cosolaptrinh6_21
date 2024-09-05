def Input():
    n=int(input('n='))
    L=[]
    for i in range (n):
        a=int(input())
        L=L+[a]
    return(L)
def FirstAndLast(L):
    A=[]
    A=[L[0],L[-1]]
    print(A)
    return A
def Search(L,x):
    if x in L:
        k=1    
    else:
        k=0
    return(k)
L=Input()
x=int(input('x='))
A=FirstAndLast(L)
k=Search(L,x)
if k==1:
    print('True')
else:
    print('False')