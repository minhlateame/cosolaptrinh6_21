def LaSoNguyenTo(x):
    k=1
    for i in range(2,x):
        if x%i==0:
            k=k+1
    if k>1:
        return(False)
    else:
        return(True)
                   
def SoHopLe(x):
    if x<=1:
        return(True)
    else:
        return(False)

def NhapVaDem():
    print('Nhap day so:')
    t=0
    while True:
        x=int(input())
        if SoHopLe(x)==True:
            break
        elif LaSoNguyenTo(x)==True:
            t=t+1
    return(t)
def inKQ(kq):
    print('Co',kq,'so nguyen to')
kq=NhapVaDem()
inKQ(kq)
    