n=int(input('n='))
if 0<=n<=100:
    s=1
    i=1
    for i in range (i,n):
        s=s+(s*i)
        i=i+1
    print(n,'!=',s,sep="")
else :
    print(' Nhap Lai')