import math
a=int(input('Nhap a='))
b=int(input('Nhap b='))
c=int(input('Nhap c='))
if a==0:
    if b==0:
        if c==0:
            print('Phuong Trinh vo so nghiem')
        else :
            print('Phuong Trinh vo nghiem')
    else:
        print('Phuowng Trinh co ngiem = ',-b/a)
else:
    d=b*b-4*a*c
    if d==0:
        print('Phuong Trinh co nghiem Co nghiem kep x1=x2= ',-b/2*a)
    elif d<0:
        print('Phuong Trinh vo nghiem')
    elif d>0:
        print('Phuong Trinh Co hai nghiem phan biet: x1=',(-b+ math.sqrt(d))/(2*a),'x2=',(-b-math.sqrt(d))/(2*a))
    