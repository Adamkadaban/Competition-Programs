def join(stuff):
  r=set(stuff[0])
  for i in range(1,len(stuff)):
    r={_ for _ in r if _ in stuff[i]}
  return list(r)

fin=open("gymnastics.in")
s, c=map(int, fin.readline().rstrip().split())

data=[]
for i in range(s):
  cows=list(map(int, fin.readline().rstrip().split()))
  data.append(cows)
fin.close()

outData=[]

for i in range(1, c+1):
  ans=[]
  for sec in data:
    pos=sec.index(i)
    ans.append(tuple(sec[pos+1:]))
  outData.append([i, join(ans)])

tot=sum([len(i[1]) for i in outData])


fout=open("gymnastics.out", "w")
fout.write(str(tot)+"\n")
fout.close()



