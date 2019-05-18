def getAns(n):
  n=int(n)
  arr=[n]
  while arr[-1]!=1:
    if arr[-1]%2==0:
      arr.append(arr[-1]//2)
    else:
      arr.append(arr[-1]*3+1)
  return str(len(arr))

fin=open("Prob05.in.txt")
N=int(fin.readline())
for i in range(N):
  n=fin.readline().strip()
  print(n+":"+getAns(n))
fin.close()