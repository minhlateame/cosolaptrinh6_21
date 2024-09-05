n=input().split(',')
c=[]
a=[x for x in n]
for i in a:
   k= int(i,2)
   if k%3==0:
        c.append(i)
h=",".join(c)
print(h)
