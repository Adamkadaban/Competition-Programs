def isHarshad(x):
  tot=0
  ne=str(x)
  for i in ne:
    tot+=int(i)
  if x%tot==0:
    return True
  return False
n=int(input())

while not isHarshad(n):
  n+=1
print(n)