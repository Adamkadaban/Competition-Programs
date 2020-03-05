def before(li, num1, num2):
  for i in li:
    if i==num1:
      return num1
    if i==num2:
      return num2
  return -1

a, b = map(int, input().split())

nums=list(map(int, input().split()))

x=[]
for i in nums:
  if i not in x:
    x.append(i)

frequency={}

for i in x:
  frequency[i]=nums.count(i)

sortedF=sorted(frequency.items(), key=lambda kv: kv[1], reverse=True)

# print(sortedF)

outp=[]
for i in sortedF:
  rangeNum=i[1]
  for j in range(rangeNum):
    outp.append(i[0])

print(*outp)