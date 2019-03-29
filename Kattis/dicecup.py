a,b=map(int, input().split())
s=min(a,b)
b=max(a,b)
for i in range(s+1,b+2):
  print(i)