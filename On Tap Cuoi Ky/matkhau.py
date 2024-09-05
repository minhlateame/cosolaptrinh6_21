n=input()
a=0
b=0
c=0
d=0
if len(n)<6:
    for i in n:
        if i.isupper:
            a=a+1
        elif i.islower:
            b=b+1
        elif i.isnumeric:
            c=c+1
    if a>0 or b>0 and c>0:
        print('Hop le')
    else:
        d=d+1
        print('khong hop le')
else:
    d=d+1
    print('Khong hop le')
if d>5:
    print('Thoat chuong trinh ')