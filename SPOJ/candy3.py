T=int(input())
ins=[]
for i in range(T):
  input()
  n=int(input())
  subins=[]
  for j in range(n):
    subins.append(int(input()))
  ins.append(subins)

for i in ins:
  if sum(i)%len(i)==0:
    print("YES")
  else:
    print("NO")