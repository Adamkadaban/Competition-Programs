def getAns(x, y):
  a=x%y
  b=x//y
  return str(b)+" "+str(a)+" / "+str(y)
x, y = map(int, input().split())
while x+y!=0:
  print(getAns(x, y))
  x, y = map(int, input().split())