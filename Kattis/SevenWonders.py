x=input()
T=x.count("T")
C=x.count("C")
G=x.count("G")
tot=T**2+C**2+G**2
if T>0 and C>0 and G>0:
  p=min(T, C, G)*7
  tot+=p
print(tot)