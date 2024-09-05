import math
n=int(input())
s=0
if n<2:
    print('NO')
elif n==2:
    print('YES')
elif n>2:
    if n%2!=0:
        for i in range(3,int(math.sqrt(n))+1):
            if n%i==0:
                s=s+1
        if s==0:
            print('YES')
        else:
            print('NO') 
    else:
        print('NO')
              