i=1
n=str(input('Nhap day so:'))
while i<=10:
    o=int(input(''))
    print('')
    i=i+1
x=int(input('x='))
l=[]
l=l+[o]
for i in range (0,len(l)):
    if l[i]==5:
        l[i]=x
print(l)