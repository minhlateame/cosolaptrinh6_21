n=input()
a=n.split(' ')
s=0
x=int(input())
for i in range(0,len(a)):
    if (int(a[i]))==x:
        print(i+1)
    else:
        s=s+1
        if s==len(n):
            print('0')
