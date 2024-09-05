def Input():
    n=int(input('n='))
    L=[]
    for i in range (n):
        a=int(input())
        L=L+[a]
    return(L)
def SND(L):
    k=0
    for i in range (len(L)):
        if L[i]>0:
            k=k+1
    return(k)
def TBC(L):
    b=0
    t=0
    tb=0
    for i in range(len(L)):
        if L[i]%2==0:
            b=b+L[i]
            t=t+1
    if t<=0:
        t=0
    else:
        tb=b/t
    return(tb)
def output(k,tb):
    print('SND=',k,sep="")
    print('TBC=',tb,sep="")
a=Input()
b=SND(a)
c=TBC(a)
output(b,c)