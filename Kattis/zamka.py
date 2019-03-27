l=int(input())
d=int(input())
x=int(input())
small=l
big=d

it=list(range(l, d+1))

for i in it:
  if sum(list(map(int, list(str(i)))))==x:
    small=i
    break
for i in it[::-1]:
  if sum(list(map(int, list(str(i)))))==x:
    big=i
    break
print(small)
print(big)