'''
off=0
red=1
green=2
blue=3

multiply left by 4 and add to right
'''
def getColor(a):
  res=""
  d=a//4
  r=a%4
  if d==0:
    res+="off "
  if d==1:
    res+="red "
  if d==2:
    res+="green "
  if d==3:
    res+="blue "
  if r==0:
    res+="off"
  if r==1:
    res+="red"
  if r==2:
    res+="green"
  if r==3:
    res+="blue"
  return res
def getAns(a):
  n=0
  a=a.split()
  if a[0]=="BROKEN":
    n+=8
  if a[1]=="BROKEN":
    n+=4
  if a[2]=="BROKEN":
    n+=2
  if a[3]=="BROKEN":
    n+=1
  return getColor(n)
fin=open("Prob06.in.txt")
N=int(fin.readline())
for i in range(N):
  print(getAns(fin.readline().strip()))
fin.close()