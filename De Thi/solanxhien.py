n=int(input())
l=[]
d=0
for i in range(0,n):
    x=input()
    l=l+[x]
k=int(input())
if k in l:
    d=d+1
    if d==1:
        print('True')
    else:
        print('False')