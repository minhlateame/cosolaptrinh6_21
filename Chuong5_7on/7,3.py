n=str(input())
h=0
c=0
s=0
k=0
if 6<=len(n)<=17:
    for i in range(0,len(n)):
        if n[i].islower()==True:
            c=c+1
        elif n[i].isnumeric()==True:
            s=s+1
        elif n[i].isupper()==True:
            h=h+1
        elif n[i]=='$' or n[i]=='#' or n[i]=='@':
            k=k+1
    if k>0 and h>0 and c>0 and s>0:
        print('True')
    else:
        print('False')
else:
    print('False')
