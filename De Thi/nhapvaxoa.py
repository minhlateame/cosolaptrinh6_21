while True:
    b=[]
    x=input().split()
    if len(x)==0:
        break
    else:
        for i in range(len(x)):
            if x[i]==x[0]:
                continue
            else:
                b.append(x[i])
        print(len(b))

        
