input()
nums=sorted(list(map(int, input().split())), reverse=True)
most=0
for i in range(len(nums)):
  x=i+1+nums[i]
  if x>most:
    most=x

print(str(most+1))