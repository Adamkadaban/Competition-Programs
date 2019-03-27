def findDup(l):
  for i in l:
    if l.count(i)!=2:
      return str(i)
  return
x=[]
y=[]
for i in range(3):
  n=list(map(int, input().split()))
  x.append(n[0])
  y.append(n[1])

print(findDup(x)+" "+ findDup(y))