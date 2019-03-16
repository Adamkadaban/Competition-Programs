def getAns(n): 
  count = 0
  i=5
  while (n/i>=1): 
    count += int(n/i) 
    i *= 5
  return int(count) 
ins=[]
N=int(input())
for x in range(N):
  ins.append(int(input()))
for x in ins:
  print(str(getAns(x)))