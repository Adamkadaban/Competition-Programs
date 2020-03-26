n=int(input())
ppl=[]
for i in range(n):
  a,b=map(str,input().split())
  if a=="entry":
    if b in ppl:
      print(b,"entered (ANOMALY)")
      # ppl.append(b)
    else:
      ppl.append(b)
      print(b,"entered")
  else:
    if b not in ppl:
      print(b,"exited (ANOMALY)")
    else:
      ppl.remove(b)
      print(b,"exited")