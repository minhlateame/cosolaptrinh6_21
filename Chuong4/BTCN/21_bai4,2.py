def nhap():
    n=int(input('n='))
    return n
def inkq(n):
        for i in range (1,n+1):
            if i%2==0:
                print(i,end=" ")
while True: 
    n=nhap()
    kq=inkq(n)
    print("")
    ch=str(input('Tiep tuc khong?'))
    if ch=='k' or ch=='K':
        break
