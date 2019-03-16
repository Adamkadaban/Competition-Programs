n=int(input())
ins=[]
for x in range(n):
  ins.append(input())
for x in range(len(ins)):
  if(len(ins[x])>10):
    ins[x]=ins[x][0]+str(len(ins[x])-2)+ins[x][-1]
for x in ins:
  print(x)