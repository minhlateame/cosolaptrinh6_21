i=str(input())
A=list(i)
l=['u','e','o','a','i','y']
if A[0] in l:
    print(i+'way',sep="")
else:
    for i in range(1,len(A)):
        if A[i] in l:
            N=A[i:]+A[:i]
            break
    N.append('ay')
    A="".join(N)
    print(A)