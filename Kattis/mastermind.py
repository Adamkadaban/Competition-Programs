n, key, inp=map(list, input().split())
r=0
s=0
for i in range(len(key)):
  if key[i]==inp[i]:
    r+=1

for i in key:
  if i in inp:
    inp.remove(i)
    s+=1

print(r, (s-r))