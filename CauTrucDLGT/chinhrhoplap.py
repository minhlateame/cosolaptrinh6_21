# n=int(input())
# print(2**n)
# for i in range (0,n):
#     for j in range(0,2):
#         print(j)
#     print("\n")
def Tim(i,k,n,x):
    for j in range(0,n):
        x[i]=j 
        if i==k-1:
            print(x)
        else:
            Tim(i+1,k ,n, x)
x=[]
k=4
n=3
for i in range (0,k):
    x.append(0)
Tim(0,k,n,x)