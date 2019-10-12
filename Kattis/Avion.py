ind=[]
x=[]
for i in range(5):
  x.append(input())
for i in range(len(x)):
  if "FBI" in x[i]:
    ind.append((i+1))
if len(ind)>0:
  print(*ind)
else:
  print("HE GOT AWAY!") 