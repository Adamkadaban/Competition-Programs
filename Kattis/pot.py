N=int(input())
tot=0
for i in range(N):
  x=input()
  b=int(x[:-1])
  e=int(x[-1])
  tot+=b**e
print(tot)