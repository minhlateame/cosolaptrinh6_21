def nhap():
    print('Nhap 3 so nguyen:')
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c
def max3(a,b,c):
    m=a
    if m<b:
        m=b
    if m<c:
        m=c
    return m
def inkq(kq):
    print('So lon nhat la:',kq)
    
a,b,c=nhap()
kq=max3(a,b,c)
inkq(kq) 