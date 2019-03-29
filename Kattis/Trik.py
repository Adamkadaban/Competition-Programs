x=[1,0,0]
n=input()
for i in range(len(n)):
  if n[i]=='A':
    x[0],x[1]=x[1],x[0]
  if n[i]=='B':
    x[1],x[2]=x[2],x[1]
  if n[i]=='C':
    x[0],x[2]=x[2],x[0]
print(x.index(1)+1)