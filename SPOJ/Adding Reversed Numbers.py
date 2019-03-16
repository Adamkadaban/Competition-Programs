N=int(input())
for i in range(N):
  max=input().split()
  print((str(int(max[0][::-1]) + int(max[1][::-1]))[::-1]).lstrip("0"))
  