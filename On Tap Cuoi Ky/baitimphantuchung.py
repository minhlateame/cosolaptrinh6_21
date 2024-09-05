A=str(input()).split()
B=str(input()).split()
C=[]
for i in range(1,len(A)):
    if A[i] in B:
        C=C+[A[i]]
print(*C)
