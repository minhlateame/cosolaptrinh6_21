n=input()
B=['#','!','^','"','%']
L=[]
for i in range(0,len(n)):
    if n[i] not in B:
        L.append(n[i])
        K=''.join(L)
print(K)