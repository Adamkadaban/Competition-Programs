L, x = map(int, input().split())
tot=0
r=0
for i in range(x):
  w, p=input().split()
  p=int(p)
  if w=="enter":
    tot+=p
    if tot>L:
      r+=1
      tot-=p
  else:
    tot-=p
print(r)