n=int(input())
x=input().split()
a=[]
for i in range(len(x)):
    if n==int(x[i]):
        a=a+[i]
print(a)
    