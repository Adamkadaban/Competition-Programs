cows=sorted(["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy","Sue"])

inp=[]
fin=open("lineup.in")
N=int(fin.readline().rstrip())
for i in range(N):
  inp.append(fin.readline().rstrip())
fin.close()

data = []

def isThing(a, li):
  return a == li[0] or a == li[-1]

def inPos(a, lists):
  for li in lists:
    if a in li:
      return True
  return False

def inArr(a, lists):
  for li in lists:
    if isThing(a, li):
      return True
  return False

def put(a, b, li):
  if a == li[0]:
    li.insert(0, b)
  elif a == li[-1]:
    li.append(b)
  elif b == li[0]:
    li.insert(0, a)
  elif b == li[-1]:
    li.append(a)

def join(a, b, c, d):
  if a!=c[-1]:
    c.reverse()
  if b!=d[0]:
    d.reverse()
  return c + d



def insert(a, b, stuff):
  ab = inArr(a, stuff)
  ba = inArr(b, stuff)
  if (not ab) and (not ba):
    stuff.append([a, b])
    return
  elif ab+ba==1:
    for li in stuff:
      put(a, b, li)
    return
  aL = []
  bL = []
  for li in stuff:
    if isThing(a, li):
      aL = li
    if isThing(b, li):
      bL = li
  stuff.remove(aL)
  stuff.remove(bL)
  aabb = join(a, b, aL, bL)
  stuff.append(aabb)


def sortMe(aa):
  if aa[0] > aa[-1]:
    aa.reverse()





for line in inp:
  words = line.split()
  a = words[0]
  b = words[5]
  insert(a, b, data)


for name in cows:
  if not inPos(name, data):
    data.append([name])


for _ in data:
  sortMe(_)

data.sort()

fout=open("lineup.out", "w")
for li in data:
  for a in li:
    fout.write(a+"\n")
fout.close()