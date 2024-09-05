n=str(input())
b=[]
ns=[]
c=[]
ns=n.strip()
b=ns.split()
for i in range(0,len(b),1):
    if i==0:
        c.append(b[0].title())
    else:
        c.append(b[i].lower())
ns=' '.join(c)
ns=ns.replace(' ,',',')
ns=ns.replace(' :',':')
ns=ns.replace(' .','.')
ns=ns.replace(' ;',';')
print(ns)
