n = int(input("Nhap n"))
i = 1
print(i, end=" ")
while i <= n:

    if i + 1 <= n:
        i += 1
        print(i, end=" ")
    if i + 3 <= n:
        i += 3
        print(i, end=" ")
    if i + 5 <= n:
        i += 5
        print(i, end=" ")
    else:
        break