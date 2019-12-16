#TLE - doesn't work
fin=open("moobuzz.in")
N=int(fin.readline().rstrip())
fin.close()

realNum=0
c=0
while c!=N:
  if realNum%3!=0 and realNum%5!=0:
    c+=1
  realNum+=1  

realNum-=1
with open("moobuzz.out", "w") as fout:
  fout.write(str(realNum)+"\n")  