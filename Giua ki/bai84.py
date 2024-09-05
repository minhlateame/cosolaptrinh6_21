def nhap():
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c
def trungbinh(a,b,c):
    if a<b and b<c:
        t=b
    if b<a and a<c:
        t=a
    if a<c and c<b:
        t=c
    return t    
def inkq(t):
    print('So trung vi',t)
x,y,z=nhap()
h=trungbinh(x,y,z)
inkq(h)