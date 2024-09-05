 bai1+bai2
def tongdequy(x):
    if x==0:
         return 0
     return x+tongdequy(x-1)
 def tongkodequy(x):
     for i in range(1,x):
         x=x+i
     return x
n=int(input())
bd=time.time()
 print(tongdequy(n))
print(tongkodequy(n))
 kt=time.time()
 tg=kt-bd
print(tg)
bai3+bai4
def tichdequy(x):
     if x==0:
         return 1
     return x*tichdequy(x)
def tichkodequy(x):
     for i in range(x-1,1,-1):
         x=x*i
     return x
 n=int(input())
 print(tichkodequy(n))
bai5+bai6
 import math
 def InNTdequy(n):
    if (n==2):
        print(n)
     else:
         s=0
         for j in range (2,int(math.sqrt(n))+1):
            if( n%j == 0):
                s=s+1
        if (s==0):
            print (n)
        InNTdequy(n-1)
 n=int(input())
 print(InNTdequy (n))
bai6
 n=int(input())
def Lasonguyento(n):
    s=0
   for i in range(2,n+1):
         if n%i==0:
             s=s+1
    if s==1:
        return True
   else:
        return False
 for i in range(2,n+1):
    if Lasonguyento(i)==True:
        print(i)
         Bài7: viết chương trình tính dãy Fibonaci
 n=int(input())
 L=[0,1]
 for i in range(1,n-1):
     a=L[i]+L[i-1]
    L=L+[a]
 print(*L)

Bài8: viết chương trình in xâu đảo ngược không đệ quy
s=input("")
 newS=""
 for i in s:
     newS=i+newS
 print(newS)
