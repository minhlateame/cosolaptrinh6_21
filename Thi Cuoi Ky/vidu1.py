# def LinearSearch(a, n, x):
#     i=0
#     while(i<n and a[i]!=x):
#         i+=1
#     if (i<n):
#         print (i)
#     else:
#          print("Khong tim thay")
# n=24
# a=[7,13,5,21,6,2,8,15]
# x=5
# LinearSearch(a,n,x)
def F(n):
    if (n==1 or n==2):
        return 1
    else:
       return F(n-1)+F(n-2)
        
n=10
print(F(n))