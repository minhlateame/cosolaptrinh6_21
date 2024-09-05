n=input()
b=list(n)
a=0
for i in range(len(b)):
   a=a+int((b[i]))**len(b)
if int(n)==a:
    print('True')
else:
    print('Falae')