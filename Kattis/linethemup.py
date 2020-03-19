n=int(input())
OGNames=[]
for i in range(n):
  OGNames.append(input())

inc=sorted(OGNames)
dec=inc[::-1]

if OGNames==inc:
  print("INCREASING")
elif OGNames==dec:
  print("DECREASING")
else:
  print("NEITHER")