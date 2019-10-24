import math
r, c = map(int, input().split())

area1=math.pi*(r-c)**2
area2=math.pi*(r)**2

res=area1/area2

print(res*100)