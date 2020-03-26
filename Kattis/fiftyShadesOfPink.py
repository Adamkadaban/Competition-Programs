c=0
for i in range(int(input())):
  x=input()
  x=x.lower()
  if "pink" in x or "rose" in x:
    c+=1
if c>0:
  print(c)
else:
  print("I must watch Star Wars with my daughter")