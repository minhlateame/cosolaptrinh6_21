import math
a,b,c=map(int,input("").split())
s=(a+b+c)/2
if a+b>c and a+c>b and b+c>a:
    n=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(a+b+c,'{:.2f}'.format(n))
else:
    print('NO')