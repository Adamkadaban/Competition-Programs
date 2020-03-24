a, b = map(int, input().split())
ins=[]
for i in range(a):
  ins.append(list(input()))


def flood(arr, x, y):
  c=0
  if x>=len(arr[0]):
    return 0
  if x<0:
    return 0
  if y<0:
    return 0
  if y>=len(arr):
    return 0

  if arr[y][x]=="." or arr[y][x]=="X":
    return 0
  if arr[y][x]=="#":
    arr[y][x]="X" #2=Visited
    c+=1  
    # c+=flood(arr, x+1, y)
    # c+=flood(arr, x, y+1)
    # c+=flood(arr, x-1, y)
    # c+=flood(arr, x, y-1)
    # c+=flood(arr, x+1, y+1)
    # c+=flood(arr, x-1, y-1)
    # c+=flood(arr, x-1, y+1)
    # c+=flood(arr, x+1, y-1)
    for _ in range(-1, 2):
      for __ in range(-1, 2):
        c+=flood(arr, x+_, y+__)

  return c

maxSize=0
numIslands=0
for i in range(len(ins)):
  for j in range(len(ins[0])):
    t=flood(ins, j, i)
    if t>maxSize:
      maxSize=t
    if t>0:
      numIslands+=1

print(numIslands)