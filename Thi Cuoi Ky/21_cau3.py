n=input().split(' ')
a=[]
b=0
for i in range(len(n)):
    if n[i] not in a:
        a=a+[n[i]]
        b=b+1
print(b)
        