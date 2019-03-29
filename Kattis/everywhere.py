T=int(input())
for i in range(T):
  x=[]
  N=int(input())
  for j in range(N):
    c=input()
    if c not in x:
      x.append(c)
  print(len(x))