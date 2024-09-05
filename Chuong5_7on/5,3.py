n=int(input('n='))
i=0
t=0
b=0
s=1
a=0
while i<n:
    x=int(input())
    if x>0:
        t=t+1
        if x%2==0:
            b=b+t
            a=a+1
    i=i+1
if b==0:
    s=0
else:
    s=b/a
print('SND=',t,sep=(''))
print('TBC=',s,sep=(''))
