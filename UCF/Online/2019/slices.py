import sys
def getRealAns(stuff):
  KHJ= len([_ for _ in stuff if _=="Kelly hates Jim"])
  JHK= len([_ for _ in stuff if _=="Jim hates Kelly"])
  if KHJ+JHK==0:
    return "Everything is good"
  if KHJ>0 and JHK>0:
    return "Their friendship is doomed"
  if JHK>KHJ:
    return "Jim hates Kelly"
  if KHJ>JHK:
    return "Kelly hates Jim"
def getAns(ja, kels, k):
  if ja>kels +k:
    return "Kelly hates Jim"
  if kels>ja+k:
    return "Jim hates Kelly"
for i in range(int(sys.stdin.readline())):
  stuffs=[]
  n,k=map(int, input().split())
  jTot=0
  kellyTot=0
  for j in range(n):
    name, move=map(str, input().split())
    move=int(move)
    if name=="Jim":
      jTot=move
    else:
      kellyTot=move
    stuffs.append(getAns(jTot, kellyTot, k))
  print(getRealAns(stuffs))


    