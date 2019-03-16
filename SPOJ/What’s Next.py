def isAP(arr):
  if (arr[1]-arr[0]) == (arr[2]-arr[1]):
    return True,arr[1]-arr[0]
  return False, arr[1]//arr[0]
def inp():
  return list(map(int, input().split()))
r=[inp()]
outs=[]
end=[0,0,0]
while r[-1] != end:
  r.append(inp())
for i in range(len(r)):
  if isAP(r[i])[0]:
    outs.append("AP " + str(r[i][-1]+isAP(r[i])[1]))
  else:
    outs.append("GP "+ str(r[i][-1]*isAP(r[i])[1]))
for x in outs[:-1]:
  print(x)