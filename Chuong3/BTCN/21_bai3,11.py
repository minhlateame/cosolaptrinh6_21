k=0
s=1
i=1
n=int(input())
#for i in range(1,n+1):
while i!=0:
    n=int(input())
    if n>0 :
        s=s+1    
    elif n<0:
        k=k+1
    elif n==0:
        print(s,'so duong')
        print(k,'so am')