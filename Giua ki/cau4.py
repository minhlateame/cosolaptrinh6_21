n=int(input())
if n<10:
    print('0')
else:
    s=n%10
    x=n//10
    k=x%10
    print(s+k)