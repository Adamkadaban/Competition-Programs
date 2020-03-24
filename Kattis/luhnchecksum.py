def convert(n):
  n*=2
  if n>9:
    a=(n//10)
    b=n%10
    n=a+b
  return n
def getAns(arr):
  l=len(arr)
  # for i in range(len(arr)):
  #   if l%2==0:
  #     if i%2==0:
  #       arr[i]=convert(arr[i])
  if l%2==0:
    for i in range(len(arr)):
      if i%2==0:
        arr[i]=convert(arr[i])
  else:
    for i in range(len(arr)):
      if i%2==1:
        arr[i]=convert(arr[i])
  return (sum(arr))%10==0

N=int(input())
for i in range(N):
  _=list(map(int, list(input())))
  print("PASS" if getAns(_) else "FAIL")

# print(convert(8))