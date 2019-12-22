def getAns(nums):
  x={}
  for i in nums:
    if i in x:
      x[i]+=1
    else:
      x[i]=1
  for i in list(x.items()):
    if i[1]==1:
      return i[0]
N=int(input())
for i in range(N):
  input()
  x=list(map(int, input().split()))
  r=getAns(x)
  print("Case #"+str(i+1)+": "+str(r))