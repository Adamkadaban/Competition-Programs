#Doesn't work
fin=open("moobuzz.in")
N=int(fin.readline().rstrip())
fin.close()

def getAns(N):
  return N-((N-N%3)/3) - ((N-N%5)/5) + ((N-N%15)/15)


def search(small, big, goal):
  mid=(small +big)//2
  if getAns(mid)==goal:
    return mid
  elif getAns(mid)<N:
    return search(mid, big, N)
  else:
    return search(small, mid, N)

r=int(search(0, 10E9, N))
with open("moobuzz.out", "w") as fout:
  fout.write(str(r)+"\n")  