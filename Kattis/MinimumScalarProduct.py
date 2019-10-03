def getDotProd(x, y):
  s=0
  for i in range(len(x)):
    s+=x[i]*y[i]
  return s
T=int(input())
for i in range(T):
  input()
  a=list(map(int, input().split()))
  a=sorted(a)
  b=list(map(int, input().split()))
  b=sorted(b, reverse=True)
  s=getDotProd(a, b)
  print("Case #"+str(i+1)+": "+str(s))
