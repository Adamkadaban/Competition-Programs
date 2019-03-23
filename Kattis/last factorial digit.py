def factorial(n):
  prod=1
  for i in range(1, n+1):
    prod*=i
  return prod

N=int(input())
for i in range(N):
  print(str(factorial(int(input())))[-1])