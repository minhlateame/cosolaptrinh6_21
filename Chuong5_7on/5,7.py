n=int(input('n='))
a=[]
b=[]
for i in range(0,n,1):
    x=str(input())
    a=a+[x]
for i in range(0, len(a)-1,1):
    if a[i]==a[i+1]:
        b=b+[a[i]]
    #else:
        #b=b+[a[i]]+[a[i+1]]
print(b)
    