import math
l,v=map(int,input().split())
v=math.radians(v)
x=l/math.sin(v)
print(int(x+1))