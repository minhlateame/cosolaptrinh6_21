a=float(input())
b=float(input())
c=float((input()))
tb=(a+b+c)/3
if tb<5:
    print(round(tb,2))
    print('Yeu')    
elif 5<=tb<6.5:
    print(round(tb,2))
    print('Trung binh')
elif 6.5<=tb<8:
    print(round(tb,2))
    print('Kha')
elif 8<=tb<9:
    print(round(tb,2))
    print('Gioi')
elif tb>=9:
    print(round(tb,2))
    print('Xuat sac')