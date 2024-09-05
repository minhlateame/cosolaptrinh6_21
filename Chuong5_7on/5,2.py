def Input():
    n=int(input('n='))
    i=0
    l=[]
    while i<n:
        x=input()
        i=i+1
        l=l+[x]
    return(l)
def Search(l):
    i=0
    max=l[0]
    for i in range(len(l)):
        if l[i]>max:
            max=l[i]
        else:
            max=max
    min=l[0]
    for i in range (len(l)):
        if l[i]<min:
            min=l[i]
        else:
            min=min
    return(max,min)
def Output(max,min):
    print(max,min)
l=Input()
b,d=Search(l)
c=Output(b,d)
        
        