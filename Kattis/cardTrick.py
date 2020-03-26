for i in range(int(input())):
  n=int(input())
  d=[]
  d.append(n)
  for j in range(n-1, 0, -1):
      for __ in range(j):
          d.insert(0,d.pop(-1))
      d.insert(0,j)
      d.insert(0,d.pop(-1))
  print(*d)