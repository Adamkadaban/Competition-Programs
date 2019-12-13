import sys, string
def convertBase(num,b):
  rem=num%b
  div=num//b
  c=str(rem)
  while(div>0):
    rem=div%b
    div=div//b
    c=str(rem)+c
  return int(c)

def getAns(g, d):
  g=str(g)
  d=str(d)
  if g==d:
    return 10
  minBase=10
  maxBase=sys.maxsize
  mid=(minBase+maxBase)//2
  converted = sum([int(g[i])*(mid**(len(g)-i-1)) for i in range(len(g))])
  while converted!=g:
    mid=(minBase+maxBase)//2
    # converted=convertBase(d, mid)
    converted = sum([int(g[i])*(mid**(len(g)-i-1)) for i in range(len(g))])
    if int(converted)==int(d):
      break
    if int(converted)<int(d):
      minBase=mid+1
    if int(converted)>int(d):
      maxBase=mid-1
  return mid 

  
  

N=int(sys.stdin.readline())
for i in range(N):
  g, d = map(int, sys.stdin.readline().rstrip().split())
  sys.stdout.write("Hotel Visit #"+str(i+1)+": Base "+str(getAns(g, d))+"\n")

# print(convertBase(18, 13))

# print(convertBase(18, 13))