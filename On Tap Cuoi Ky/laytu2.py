n=str(input())
c=n[:2]
d=n[-2:]
if len(n)>=2:
    print(''.join(c+d))