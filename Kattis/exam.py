n=int(input())
a=input()
b=input()
same=0
for i in range(len(a)):
  if a[i]==b[i]:
    same+=1

if min(same, n)<n:
  print(str(len(a)-n+same))
else:
  print(str(n+len(a)-same))