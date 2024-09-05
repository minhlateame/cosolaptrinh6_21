# n=str(input())
# a=n.split()
# # B=[]
# # i=0
# # # while i<len(n):
# # #     B=B+[n]
# # #     i=i+1
# # # print(B)
# # for i in range (len(n),0,-1):
# #     B=B+[n[i]]
# # print(B)
# c=a.reverse()
# print(c)
n=int(input())
a=list(str(n))
a.reverse()
for i in range(0,len(a)):
    if int(a[0])==0:
        del(a[0])
    else:
        break
b=''.join(a)
print(b)
