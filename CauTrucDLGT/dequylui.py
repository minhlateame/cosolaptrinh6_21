def gt(n):
    if n==0: return 1
    return n*gt(n-1)
n=int(input("Nhap n"))
k=int(input("Nhap k"))
print("Hoán vị của ",n," là ", gt(n))
#print("tổ hợp chập ",k," của ",n," là ",gt(n)/(gt(k)*gt(n-k)))
#print("chỉnh hợp chập ",k," của ",n," là ", gt(n)/gt(n-k))
xau=input('Xau: ')
print(xau[::-1])
