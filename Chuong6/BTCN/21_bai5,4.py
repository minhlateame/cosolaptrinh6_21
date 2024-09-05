n=int(input('n='))
L=[]
for i in range (n):
    a=str(input())
    L=L+[a]
L.sort(reverse=True)
print(L)
L.reverse()
print(L)