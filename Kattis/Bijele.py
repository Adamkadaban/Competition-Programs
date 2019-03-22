ins=list(map(int, input().split()))
ps=[1,1,2,2,2,8]
r=[]
for i in range(6):
  r.append(ps[i]-ins[i])
for i in r:
  print(str(i), end=" ")