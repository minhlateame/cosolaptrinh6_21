n=input()
a=0
b=0
c=0
d=0
if 6<=len(n)<=17:
    for i in n:
        if i.isupper()==True:
            a=a+1
        elif i.isnumeric()==True:
            b=b+1
        elif i.islower()==True:
            c=c+1
        elif i=='#' or i=='@' or i=='$':
            d=d+1
    if a>0 and b>0 and c>0 and d>0:
        print('True')
    else:
        print('False')
else:
    print('False') 
