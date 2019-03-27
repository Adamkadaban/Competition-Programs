while True:
  x=int(input())
  if x!=-1:
    ins=[]
    tot=0
    for i in range(x):
      ins.append(list(map(int, input().split())))
      if i==0:
        tot+=ins[i][0]*ins[i][1]
      else:
        corrT=ins[i][1]-ins[i-1][1]
        tot+=ins[i][0]*corrT
    print(str(tot)+" miles")
  else:
    break