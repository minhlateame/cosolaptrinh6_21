n=int(input())
i=2
s=0
#for i in range(2,n+1): 
while i<=n:
    s=s+1/i
    i=i+1
print('{:.4f}'.format(s)) #làm tròn tới chữ số thứ 4 mà cần hiện những con số 0 đằng sau