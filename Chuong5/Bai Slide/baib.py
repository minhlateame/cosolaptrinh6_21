A=[]
x=int(input('x='))
print('Nhap day so')                                
for i in range(1,11):
    a=int(input())                             
    A=A+[a]
i=0
while i<len(A):
    if A[i]==x:
       del(A[i])
    else:
        i=i+1
print(A)