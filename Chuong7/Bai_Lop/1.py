a=input("")
b=input("") 
while True:
    if a.isdecimal() and b.isdecimal():
        print(int(a)+int(b))
        break
    else:
        a=input()
        b=input()