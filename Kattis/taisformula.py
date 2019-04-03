s=0
N=int(input())
v=[]
for i in range(N):
  v.append(list(map(float, input().split())))

for i in range(len(v)-1):
  t=(v[i][1]+v[i+1][1])/2
  s+=(t*(v[i+1][0]-v[i][0]))
print(s/1000)