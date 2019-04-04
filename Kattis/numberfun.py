def add(a,b,c):
  if a+b==c:
    return True
  return False
def sub(a,b,c):
  if abs(a-b)==c:
    return True
  return False
def div(a,b,c):
  if a/b==c or b/a==c:
    return True
  return False  
def mult(a,b,c):
  if a*b==c:
    return True
  return False  
def getAns(x):
  if add(*x) or sub(*x) or div(*x) or mult(*x):
    return True
  return False
N=int(input())
for i in range(N):
  x=list(map(int, input().split()))
  print("Possible" if getAns(x) else "Impossible")