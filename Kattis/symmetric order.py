def printArr(c,arr):
  print("SET",str(c))
  for i in arr:
    print(i)
def newList(n):
  x=n[::-1]
  r=[]
  for i in range(len(x)):
    if i%2==0:
      r.append(x[i])
    else:
      r.insert(0,x[i])
  if len(n)%2==0:
    return r
  return r[::-1]
c=1
while True:
  x=int(input())
  li=[]
  if x!=0:
    for i in range(x):
      li.append(input())
    r=newList(li)
    printArr(c,r)
    c+=1
  else:
    break
    