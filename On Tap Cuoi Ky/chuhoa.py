# n=input()
# if n[-1].isupper():
#     d=1
# else:
#     d=0
# for i in range (len(n)):
#     if n[i].isupper() and n[i-1].islower():
#         d=d+1
#     # elif n[-1].isupper:
#     #     d=d+1
#     # else:
#     #     d=d
# print(d)
n=list(input())
a=[]
d=0
h=0
for i in range(0,len(n)):
    if n[i].isupper()==True and n[i-1].islower()==True:
        d=d+1
    elif n[i].isupper()==True:
        h=h+1   
if h==len(n):
    print('1')
elif n[len(n)-1].isupper()==True:
    print(d+1)
else:    
    print(d)