import time
def gt_koDq(n):
    A=1
    for i in range (1,n+1):
        A=A*i
    return A
def gt_DQ(n):
    if n==0:
        return 1
    return n*gt_DQ(n-1)
n=1000
bd=time.time()

print(f"{n}!={gt_DQ(n)}")
kt=time.time()
tg=kt-bd
print("-----thoi gian",tg,end="")