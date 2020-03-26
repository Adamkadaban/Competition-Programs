def bubbleSort(x):
  c=0
  isSorted=False
  l=len(x)-1
  while not isSorted:
    isSorted=True
    for i in range(0, l):
      if x[i]>x[i+1]:
        x[i], x[i+1]=x[i+1], x[i]
        c+=1
        isSorted=False
    l-=1
  return c

n=int(input())
for i in range(n):
  nums=list(map(int, input().split()))
  nums=nums[1:]
  print((i+1),bubbleSort(nums))