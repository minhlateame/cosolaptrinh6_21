n=int(input())
i=0
l=[]
a=[]
for i in range(0,n):
    x=input()
    l=l+[x]
for i in l:
    if len(i)>len(a):
        a=i
print(len(a))
print(a)
   
    