x=float(input('x='))
y=float(input('y='))
ch=str(input('Phep toan:'))
if ch=='+' :
    print(str(x)+'+'+str(y)+'=',round(x+y,1),sep="")
elif ch=='-':
    print(str(x)+'-'+str(y)+'=',round(x-y,1),sep="")
elif ch=='*':
    print(str(x)+'*'+str(y)+'=',round(x*y,1),sep="")
elif ch=='/':
    if y==0:
        print('Khong hop le')
    else :
        print(str(x),ch,str(y)+'=',round((x/y),1),sep="")
else: 
    print('Khong hop le') 
