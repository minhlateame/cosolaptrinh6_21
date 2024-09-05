n=input()
a=0
e=0
k=0
o=0
u=0
for i in range(len(n)):
    if n[i]=='a':
        a=a+1
    elif n[i]=='e':
        e=e+1
    elif n[i]=='i':
        k=k+1
    elif n[i]=='o':
        o=o+1
    elif n[i]=='u':
        u=u+1
print(a)
print(e)
print(k)
print(o)
print(u)