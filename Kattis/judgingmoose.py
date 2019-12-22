l, r = map(int, input().split())
if l+r==0:
  print("Not a moose")
else:
  if l!=r:
    print("Odd",max(l, r)*2)
  else:
    print("Even",l*2)
