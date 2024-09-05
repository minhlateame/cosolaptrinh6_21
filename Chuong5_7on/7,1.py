n=str(input())
h=0
t=0
s=0
k=0
for i in range(0,len(n),1):
    if n[i].isupper()==True:
        h=h+1
    elif n[i].islower()==True:
        t=t+1
    elif n[i].isnumeric()==True:
        s=s+1
    else:
        k=k+1
print('In hoa:',h)
print('In thuong:',t)
print('Chu so:',s)
print('Khac:',k)
    
        
    