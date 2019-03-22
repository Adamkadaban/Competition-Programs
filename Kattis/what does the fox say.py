ins=[]
T=int(input())
for i in range(T):
  sounds=input().split()
  temp=[]
  x=input()
  temp.append(x.split()[-1])
  while x!="what does the fox say?":
    inw=input()
    temp.append(inw.split()[-1])
    x=inw
  del temp[-1]
  outs=[x for x in sounds if x not in temp]
  for p in outs:
    print(p +" ", end="")