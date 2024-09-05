n=input().split(' ')
h=[]
a=0
b=[]
for i in range(len(n)):
    a=a+int(n[i])
    h=h+[a]
print(*h)   
    