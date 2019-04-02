def getAns(arr):
  r=""
  n=len(arr)
  for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
      r+=arr[j][i]
  return r
def printl(arr):
  for i in arr:
    print(i)
N=int(input())
for i in range(N):
  enc=input()
  n=int(len(enc)**.5)
  x=[['']*n for i in range(n)]
  c=0
  for i in range(n-1, -1, -1):
    for j in range(n):
      x[i][j]=enc[c]
      c+=1
  print(getAns(x))
   