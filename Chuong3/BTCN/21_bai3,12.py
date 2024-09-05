# n=int(input())
# i=1
# for i in range (0,n+1):
#     if i==0:
#         print('A',end="")
#     elif i==1:
#         print('B',end="")    
#     elif i==2:
#         print('C',end="")   
#     elif i==3:
#         print('D',end="") 
#     elif i==4:
#         print('E',end="")
#     elif i==5:
#         print('F',end="")
#     elif i==6:
#         print('G',end="")
#     elif i==7:
#         print('H',end="") 
#     elif i==8:
#         print('K',end="")
#     elif i==9:
#         print('L',end="")
# i=i+1  
n = int(input())
a = list(str(n))
b = ""
if n>0 and n<=9999:
    for i in range (0,len(str(n)),1):
        ch = a[i]
        if ch == "0":
            b = b + "A"
        elif ch == "1":
            b = b + "B"
        elif ch == "2":
            b = b + "C"
        elif ch == "3":
            b = b + "D"
        elif ch == "4":
            b = b + "E"
        elif ch == "5":
            b = b + "F"
        elif ch == "6":
            b = b + "G"
        elif ch == "7":
            b = b + "H"
        elif ch == "8":
            b = b + "K"
        elif ch == "9":
            b = b + "L"
    print(b)
        