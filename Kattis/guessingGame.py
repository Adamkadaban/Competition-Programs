def getAns(arr):
  nums=[i for i in range(1, 11)]
  for i in arr:
    n=i[0]
    r=i[1][-1]
    if r=="h":
      for _ in range(n-1,len(nums)):
        nums[_]=0
    if r=="w":
      for _ in range(n):
        nums[_]=0
  # print(nums)
  if arr[-1][0] in nums:
    return "Stan may be honest"
  return "Stan is dishonest"
x=int(input())
ins=[]
while x!=0:
  response=input()
  ins.append([x,response])
  if response[-1]=="n":
    print(getAns(ins))
    ins=[]
  x=int(input())