from random import randrange
A=[]
for i in range(6):  
    n=randrange(1,50)
    A+=[n]
A.sort()
print('So may man:')
for i in A:
    print(i)