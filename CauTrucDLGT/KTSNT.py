# import time
# def KTNT(k):
#     A=0
#     for i in range(1,k+1):
#         if k%i ==0:
#             A=A+1
#         if A==2:
#             return False
#     return True
# n=100000
# bd=time.time()
# for i in range(1,n+1):
#     if KTNT(i):
#         print(i,end="")
# kt=time.time()
# tg=kt-bd
# print("tgian",tg,end="")


# import time
# def KTNT(k):
#     A=0
#     for i in range(2,int(0.5*k)):
#         if k%i ==0:
#             return False
#     return True
# n=100000
# bd=time.time()
# for i in range(1,n+1):
#     if KTNT(i):
#         print(i,end="")
# kt=time.time()
# tg=kt-bd
# print("tgian",tg,end="")
# import time
# def KTHH(k):
#     tonguoc=0
#     for i in range(1,k):
#         if k%i ==0:
#             tonguoc=tonguoc+i
           
#         if tonguoc==k:
#             return True
#     return False
# n=50000
# bd=time.time()
# for i in range(1,n+1):
#     if KTHH(i):
#         print(i,end =" ")
# kt=time.time()
# tg=kt-bd
# print("-----thoi gian",tg,end="")
import time
def KTHH(k):
    tonguoc=0
    if k%2==0:
        for i in range(1,(k//2)+1):
            if k%i ==0:
                tonguoc=tonguoc+i
            
            if tonguoc==k:
                return True
        return False
n=50000
bd=time.time()
for i in range(1,n+1):
    if KTHH(i):
        print(i,end =" ")
kt=time.time()
tg=kt-bd
print("-----thoi gian",tg,end="")