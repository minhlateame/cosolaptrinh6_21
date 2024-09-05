def gt(n):
    if n==0 :
        return 1
    return n*gt(n-1)
n=int(input())
k=int(input())

print("To hop chap",k,"cua " ,n,"phan tu la:",gt(n)/gt(n-k)*gt(k))
print("chinh hop chap",k,"cua " ,n,"phan tu la:",gt(n)/gt(n-k))
print("Hoan vi cua ",n,"la",gt(n))
