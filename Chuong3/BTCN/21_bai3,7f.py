while True:
  n=int(input())
  s=1
  i=1
  if n>=0:
    for i in range (1,n):
      s=s+(s*i)
      i=i+1
    print(s)
  else:
    break