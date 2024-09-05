while True:
    b=[]
    n=int(input())
    if n<=0:
        print('Khong Hop Le,Nhap lai!')
    else:
        for i in range(n):
            x=input()
            b=b+[x]
        a=min(b)
        c=max(b)
        print(a)
        print(c)
        break