n=int(input())
s=0
i=1
if n<=10000000:
    while i<=n:
        s=s+i
        i=i+1
    print(s)