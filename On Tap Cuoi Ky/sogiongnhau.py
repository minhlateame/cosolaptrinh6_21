n=input()
k=len(n)
for i in n:
    if n[0]==n[k-1]:
        print('Yes')
    else:
        print('No')
        