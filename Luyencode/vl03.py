n=int(input())
i=2
if 2<=n<=100000:
    s=0
    while 2<=i<=n:
        s=s+i
        i=i+1
    print(s+2*n)
        