def getAns(n):
  if n%2==0:
    return str(n)+" is even"
  return str(n)+" is odd"
N=int(input())
for i in range(N):
  print(getAns(int(input())))