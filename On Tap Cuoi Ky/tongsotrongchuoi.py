n=input()
s=0
for i in range (len(n)):
    if n[i].isnumeric() and n[i-1]!='-':
        s=s+int(n[i])
    elif n[i]=='-':
        s=s-int(n[i+1])
print(s)
    