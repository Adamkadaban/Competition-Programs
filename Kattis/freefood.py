x=[0]*365
N=int(input())
for i in range(N):
  a,b=map(int,input().split())
  for j in range(a,b+1):
    x[j-1]=1
print(x.count(1))
