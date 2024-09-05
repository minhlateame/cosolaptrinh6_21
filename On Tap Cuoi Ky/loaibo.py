n=str(input())
a=['#','%','*','!']
M=[]
for i in n:
    if i not in a:
        M=M+[i]
' '.join(M)
print(*M,end='')
# n = input()
# A = []
# for i in n:
#     if i == '#' or i == '*' or i == '!' or i == '^' or i == '%':
#         continue
#     else:
#         print(i,end='')