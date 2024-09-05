n=str(input())
a=n.split()
L=[]
for j in range(0,len(a)):
    L=L+[a[j]]
    if len(L)>=2:
        L.insert(len(L)-1,"and")
    if len(L)>=3:
        i=0
        while i<len(L):
            if L[i]=="and" and i!=len(L)-2:
                L[i]=","
            else:
                i=i+1
    for i in range(0,len(L)):
        print(L[i],end=" ")
    print()