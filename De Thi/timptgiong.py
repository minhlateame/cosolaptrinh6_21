a=input().split(' ')
b=input().split(' ')
l=[]
for i in range(0,len(a)):
    #for j in range(0,len(b)):
    if a[i] in b:
        l=l+[a[i]]
print(l)