a=['my','vi','ki']
print('Nhap ten:')
n=input()
if n in a:
    print('Ten da co trong danh sach')
else:
    a=a+[n]
    print(a)