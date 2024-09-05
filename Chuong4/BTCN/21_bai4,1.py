def Nhap():
    n=int(input('n='))
    return (n)

def giaithua(n):
    s=1
    if n>0:
        for i in range (1,n+1):
            s=(s*i)
        return(s)
    
def inkq(s):
    print(n,'!=',s,sep="")
    
n=Nhap()
s=giaithua(n)
kq=inkq(s)