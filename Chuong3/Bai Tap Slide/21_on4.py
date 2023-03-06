a=float(input('a='))
b=float(input('b='))
c=input(str(('Toan tu:')))
T=(input("Tiep tuc:"))
while c!= 'T'or c!='t':
    if c=='+':
        print(str(a)+'+'+str(b),a+b,sep="")
    elif c=='-':
        print(str(a)+'-'+str(b),a-b,sep="")
    elif c=='*':
        print(str(a)+'*'+str(b),a*b,sep="")
    elif c=='/':
        print(str(a)+'/'+str(b),a/b,sep="")
    elif T=="T" or T== "t":
    