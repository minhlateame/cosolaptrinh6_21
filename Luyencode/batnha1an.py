a,b=map(int,input('').split())
if a==0 and b==0:
    print('INF')
elif a==0 and b!=0:
    print('NO')
elif a!=0:
    x=-b/a
    print('{:.2f}'.format(x))