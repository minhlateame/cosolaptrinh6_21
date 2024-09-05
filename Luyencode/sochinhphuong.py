import math
n=int(input())
if n>=0:
    b=int(math.sqrt(n))
    if b**2==n:
        print('YES')
    else:
        print('NO')
else:
    print('NO')  