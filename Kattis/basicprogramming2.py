N, t = map(int, input().split())
ins = sorted(list(map(int, input().split())))

if t == 1:
  x = {}
  found = False
  for i in range(len(ins)):
    x[7777-ins[i]] = i
  for i in range(len(ins)):
    if not found and ins[i] in x and i != x[ins[i]]:
      print("Yes")
      found = True
  if not found:
    print("No")
if t == 2:
  if len(set(ins)) == len(ins):
    print("Unique")
  else:
    print("Contains duplicate")
if t == 3:
  m = {}
  found = False
  for i in ins:
    if i not in m:
      m[i] = 0
    m[i] += 1
  for k,v in m.items():
    if not found and v > len(ins)//2:
      print(k)
      found = True
  if not found:
    print("-1")
    
if t == 4:
  if len(ins) % 2 == 1:
    print(ins[len(ins)//2])
  else:
    print(ins[len(ins)//2 - 1], ins[len(ins)//2])
if t == 5:
  print(" ".join([str(i) for i in ins if 100 <= i <= 999]))