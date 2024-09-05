def  inpu():
    n=int(input('n='))
    l=[]
    i=0
    while i<n:
        a=input()
        i=i+1
        l=l+list(a)
    
    return(l)

def Firstandlast(l):
    a=[]
    a=[l[0],l[-1]]
    print(a)
    return(a)

def Search(l,x):
    if x in l:
        a=1
    else:
        a=0
    return(a)
c=inpu()
x=int(input('x='))
k=Firstandlast(c)
b=Search(k,c)
if b==1 :
    print('True')
else:
    print('False')
    
    
    
    
        