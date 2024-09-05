n=int(input('n='))
i=0
l=[]
while i<n:
    x=input()
    l=l+[x]
    i=i+1
l.reverse()
print(l)
l.sort()
print(l)
    