x=[]
g,s,c=map(int, input().split())

p=g*3+s*2+c

if p >= 8:
  x.append("Province")
elif p>=5:
  x.append("Duchy")
elif p>=2:
  x.append("Estate")

if p>=6:
  p-=6
  x.append("Gold")
elif p>=3:
  p-=3
  x.append("Silver")
elif p>=0:
  x.append("Copper")

x=" or ".join(x)
print(x)