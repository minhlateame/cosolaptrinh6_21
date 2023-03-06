n=int(input('n='))
i=2
for i in range(2,n//2+1):
    if n%i==0 :
        print(n,'khong la SNT')
        break
    else:
        print(n,'la SNT')
        