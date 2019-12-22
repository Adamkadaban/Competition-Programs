n, h, v = map(int, input().split())
p1=n-h
p2=n-v
if h>n-h:
  p1=h
if v>n-v:
  p2=v
n1=p1*p2*4
print(n1)