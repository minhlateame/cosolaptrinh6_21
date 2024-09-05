a=int(input())
b=int(input())
n=int(input())
#if 1<a and 1<b and 1<n and 10**91>a and 10**91>b and 10**91>n and a<109 and b<109 and n<109:
if a+b==n:
    print('+')   
elif a-b==n:
    print('-')
elif a*b==n:
    print('*')
elif b>0 and a/b==n:
    print('/')    
else:
    print('NO')