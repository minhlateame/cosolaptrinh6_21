import math
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
p=(a+b+c)/2
if (a+b)>c and (a+c)>b and (b+c)>a:
    print('Dien tich=',round(math.sqrt(p*(p-a)*(p-b)*(p-c)),3),sep="")
else:
    print('Khong hop le')