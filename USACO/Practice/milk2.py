"""
ID: adamkad1
LANG: PYTHON3
TASK: milk2
"""
from collections import OrderedDict as od
def toDict(x):
    return {i[0]:i for i in x}

def findLargest(x):
  most=-1
  for i in range(len(x)):
    if len(x[i])>most:
      most=len(x[i])
  return most

times=set()

f= open("milk2.in")
f1=open("milk2.out", "w")
N=int(f.readline())
for i in range(0,N):
  x=list(map(int, f.readline().split()))
  start=x[0]
  end=x[1]
  times.update(range(start,end))
f.close()

start=min(times)
end=max(times)

milking = []
for i in range(start,end+1):
  if i in times:
    milking.append(1)
  else:
    milking.append(0)

start = "".join(list(map(str, milking)))

stretch=start.split("0")
gap=start.split("1")
yes = findLargest(stretch)
no = findLargest(gap)

f1.write(str(yes) + " " + str(no) + "\n")
f1.close()
