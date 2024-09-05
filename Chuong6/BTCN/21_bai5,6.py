A=[]
for i in range (10):
    x=int(input())
    A=A+[x]
B=A.copy()
for i in range (0,6,2):
    B[i+1]=A[i]
    B[i]=A[i+1]
print(*B)

    