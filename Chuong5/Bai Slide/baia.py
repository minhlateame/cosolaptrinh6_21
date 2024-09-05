def nhap():
    A=[]                             
    for i in range(1,11):
        a=int(input())                             
        A=A+[a]
    return A
def kiemtra(A):
    for i in range(0,len(A)):
        if A[i]==5:
            A[i]=x
    print(A)
    return(A)
def xoapt(A):
    # for i in A:
    #     if i==x:
    #         k=A.index(i)
    #         del(A[k])
    i=0
    while i<len(A):
        if A[i]==x:
            del(A[i])
        else:
            i=i+1
    print(A)
    return(A)


A=nhap()
x=int(input('x='))
kiemtra(A)
xoapt(A)
