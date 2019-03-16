"""
ID: adamkad1
LANG: PYTHON3
TASK: barn1
"""
fin=open("barn1.in")
r=0
x=list(map(int, fin.readline().split()))
M, S, C=x[0], x[1], x[2]
stalls=[]
for x in range(C):
  stalls.append(int(fin.readline()))

stalls=sorted(stalls)

maxgap=0
for i in range(len(stalls)-1):
  if stalls[i+1]-stalls[i] > maxgap:
    maxgap=stalls[i+1]-stalls[i]-1

if M >= C:
    r = C
else:
    gaps = []
    for i in range(C-1):
      gaps.append(stalls[i+1] - stalls[i] - 1)
    gaps=sorted(gaps)
    maxgap=0
    for i in range(M-1):
      num=gaps[-1]
      del gaps[-1]
      maxgap+=num

    r=max(stalls)-min(stalls)+1-maxgap

fin.close()
fout=open("barn1.out", "w")
fout.write(str(r)+"\n")
fout.close()