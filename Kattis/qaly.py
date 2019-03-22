N=int(input())
c=0
for i in range(N):
  x=list(map(float, input().split()))
  c+=x[0]*x[1]
print(str(c))