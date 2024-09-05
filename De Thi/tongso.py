n=list(input())
c=0
for i in range(0,len(n)):
    if n[i]=='-' and n[i+1].isnumeric()==True:
        c=c-(int(n[i+1]))*2
    elif n[i].isnumeric()==True:
        c=c+(int(n[i]))
print(c)
