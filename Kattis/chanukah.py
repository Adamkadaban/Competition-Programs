def findAns(N):
  return str((N(N+3)/2))
P=int(input())
for i in range(1, P+1):
  a=int(input().split()[1])
  x=a*(a+3)/2
  print(str(i)+" "+str(int(x)))

