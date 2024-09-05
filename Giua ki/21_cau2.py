n=int(input())
k=0
for j in range (1,n+1):
    if j%3==0 and j%5==0:
        k=k+1
print(k)
            