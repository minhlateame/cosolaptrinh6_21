t=0
n=3
tb=0
i=0
#for i in range(0,n):
while i<n:
    x=int(input())
    if 0<=x<=10:
        t=t+x
        i=i+1    
    else:
        print('Khong hop le!!!')
tb=t/3
print(tb)
        