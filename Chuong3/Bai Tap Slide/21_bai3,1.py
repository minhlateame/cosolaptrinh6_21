a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
max=a
min=b
if max<b :
   if b>c:
      max=b
      if c>a: 
          min=a
      else: 
          min=c
   else: 
       max=c
       min=a
else: 
    if b>c:
        max= a 
        min=c
    else:  
       if a>c: 
           max=a
           min =c
       else: 
           max=c 
           min=a
print('SLN=',max,sep="")
print('SBN=',min,sep="")
     