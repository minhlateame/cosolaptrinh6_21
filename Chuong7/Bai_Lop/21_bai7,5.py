n=input()
c=n.split()
x=int(input())
a=0
for i in c:#range(len(c)):
    if int(c[i])==x:
        print(i+1)
    else:
        a=a+1
        if a==len(c)-1:
            print('0')
        
