def nhap():
    print('Nhap 3 so nguyen:')
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c
def giaipt(a,b,c):
    import math
    d=b**2-4*a*c
    if d<0:
        x1=x2=None
    elif d==0:
        x1=x2=-b/2*a
    elif d>0:
        x1=(-b+math.sqrt(d))/2*a
        x2=(-b-math.sqrt(d))/2*a
    return x1,x2
def inkq(x1,x2):
    if x1==x2==None:
        print('Phuong trinh vo nghiem')
    elif x1>x2 or x2>x1:
        print('Phuong trinh co hai nghiem')
        print('x1=',x1,sep="")
        print('x2=',x2,sep="")
    elif x1==x2:
        print('Phuong trinh co nghiem kep')
        print('x1=x2=',x1,sep="")
        
a,b,c=nhap()
x1,x2=giaipt(a,b,c)
inkq(x1,x2)