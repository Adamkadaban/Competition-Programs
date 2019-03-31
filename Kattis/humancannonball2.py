g=9.81
import math
N=int(input())
for i in range(N):
  vo,th,x,h1,h2=map(float, input().split())
  th=math.radians(th)

  xTime=x/(vo*math.cos(th))
  yPos=vo*xTime*math.sin(th)-((g/2)*xTime**2)

  # print(yPos)
  if (h2-1 >= yPos) and (h1+1 <=yPos):
    print("Safe")
  else:
    print("Not Safe")