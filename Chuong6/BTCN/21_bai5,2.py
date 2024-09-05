def Input():
    n=int(input('n='))
    L=[]
    for i in range (n):
        a=int(input())
        L=L+[a]
    return(L)
def Search(L):
    max=L[0]
    for i in range (len(L)):
        
        if max<L[i]:
            max=L[i]
    min=L[0]
    for i in range (len(L)):
        
        if min>L[i]:
            min=L[i]
    return(max,min)
def output(max,min):
    print(max,min)
a=Input()
b,d=Search(a)
c=output(b,d)
        
