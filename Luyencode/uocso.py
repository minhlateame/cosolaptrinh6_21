n=int(input())
if n!=0:
    for i in range(abs(n),0,-1):
        if n%i==0:
            print(i,end=' ')
else:
    print('INF')
