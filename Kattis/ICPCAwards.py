#hehehehe i guessed the code based on the input and output
n=int(input())
x=[]
y=[]
for i in range(n):
  a=input()
  b=a.split()[0]
  if (b not in y):
    x.append(a)
  y.append(b)

for i in range(12):
  print(x[i])