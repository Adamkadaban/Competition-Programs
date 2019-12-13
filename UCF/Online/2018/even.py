query = int(input())
times = 0
outs = []
while query > 0:
  level = int(input())
  factor = 0
  hyper = False
  while hyper == False:
    log = 2**factor
    if log <= level:
      factor = factor + 1
    else:
      number = abs(level - log)
      hyper = True
      times = times + 1
  outs.append("Pokemon "+str(times)+": "+str(number))
  query = query - 1
  number = 0
for x in range(len(outs)):
  print(outs[x])