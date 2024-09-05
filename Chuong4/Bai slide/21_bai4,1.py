def nhap():
    n=int(input('n='))
    return n
def nhapvadem(n):
    print('Nhap',n,' so nguyen')
    s=0
    for i in range (1,n+1):
        n=int(input())
        if n%2==0:
            s=s+1
    return s
def inkq(kq):
    print('so chu so chan la:',kq)
n=nhap()
kq=nhapvadem(n)
kq=inkq(kq)