n=input().split()
c=[]
l=[]
for i in n:
    if (int(i))%2==0:
        c=c+[int(i)]
    else:
        l=l+[int(i)]
print(c)
print(l)