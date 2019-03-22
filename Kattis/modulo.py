ins=[]
for i in range(10):
  n=int(input())%42
  if n not in ins:
    ins.append(n)
print(len(ins))