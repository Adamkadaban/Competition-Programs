def isPal(a):
  if a==a[::-1]:
    return True
  return False
def getAns(arr):
  b=True
  bad=[]
  arr=[i.lower() for i in arr]
  for i in range(len(arr)):
    b=isPal(arr[i]) and b
    if not isPal(arr[i]):
      bad.append(str(i+1))
  if b:
    return "True"
  else:
    return "False - "+", ".join(bad)

fin=open("Prob07.in.txt")
N=int(fin.readline())
for i in range(N):
  T=int(fin.readline())
  x=[]
  for i in range(T):
    x.append(fin.readline().strip())
  print(getAns(x))

fin.close()
