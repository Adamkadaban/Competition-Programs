c=0
x=input()
l=int(len(x)/3)
p="PER"*l
for i in range(len(x)):
  if x[i]!=p[i]:
    c+=1
print(c)