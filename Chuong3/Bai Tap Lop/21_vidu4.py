a=int(input('So Nam:'))
b=int(input('Salary:'))
c=0
if a<5:
    if b<500:
        c=100
    else:
        c=200
else:
    c=700
print('Bonus amount:',c)