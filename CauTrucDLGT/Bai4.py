n=int(input())
c=1
def Lasonguyento(c):
    s=0
    for i in range(2,c):
        if c%i==0:
            s=s+1
    if s==0:
        return True
    else:
        return False
while c<=n-1:
    c+=1
    if Lasonguyento(c)==True:
        print(c)