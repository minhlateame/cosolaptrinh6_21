a,b=map(int,input('').split())
print(a+b)
print(a-b)
print(a*b)
if b<=0:
    print('INF')
else:
   print('{:.2f}'.format(a/b))