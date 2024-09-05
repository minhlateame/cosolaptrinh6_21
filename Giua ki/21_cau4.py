n=int(input())
s=0
a=list(str(n))
k=len(str(n))
ch=0
if k>1:
    for i in range(k-2,k,1):
        ch=ch+int(a[i])
    print(ch)
else:
    print('0')