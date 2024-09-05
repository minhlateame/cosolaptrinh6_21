n=str(input()).split()
L=[]
if len(n)>=5:
    L=n[1]+n[3]+n[4]
elif len(n)>=4:
    L=n[1]+n[3]
elif len(n)>=2:
    L=n[1]
M=[]
for i in n:
    if i not in L:
        M=M+[i]
print(*M)