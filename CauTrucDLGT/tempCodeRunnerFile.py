import time
def KTNT(k):
    A=0
    for j in range (1,k+1):
        if k%j==0:
            A=A+1
    if A==2:
        return True
        return False
    #beginning
    # n=int(input('n='))
    n=100000
    bd=time.time()
    for i in range (1,n+1):
        if KTNT(i):
            print(i,end=" ")
    kt=time.time()
    tg=kt-bd
    print("Thoi gian :{0}",tg)