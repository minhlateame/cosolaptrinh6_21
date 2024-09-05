n=int(input(''))
i=2 
h=0
for i in range (2,n):  
    for i in range(2,i//2+1):
        if n%i==0 :
            break
        else:
            h=h+1
print(h)        
        
# n=int(input())

# c=0
# for i in range(1,n):
#     #if #i%2==0 or i%3==0 or i%4==0 or i%5==0 or:
#     j=i/2
#     if i%j==0:
#         d=0
#     else:
#         c=c+1
#     #  for j in range(1,i//2):
#     #     if i%j==0:
#     #         d=0
#     #     else:
#     #         c=c+1
# print(c)
n=int(input())
d=0
for i in range(1,n):
    if i%2!=0 or i%4!=0 or  i%4!=0 or i%5!=0 or  i%6!=0 or  i%7!=0 or  i%8!=0 or  i%9!=0 or i%10!=0:
        d=d+1
    
print(d)