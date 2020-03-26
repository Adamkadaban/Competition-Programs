def getAns(coords, xL, yL):
  a=0
  b=0
  for i in coords:
    x,y=i[0],i[1]
    if x>xL and y>yL:
      a+=1
      # print(1,x,y)
    if x<xL and y<yL:
      a+=1
      # print(2,x,y)
    if x>xL and y<yL:
      b+=1
      # print(3,x,y)
    if x<xL and y>yL:
      b+=1
      # print(4,x,y)
    # if x==xL or y==yL:
    #   print(0,x,y)
  return a,b
n=int(input())
while n!=0:
  coords=[]

  for i in range(1,n+1):
    x,y=map(int, input().split())
    coords.append([x,y])
  center=len(coords)//2
  xLine=coords[center][0]
  yLine=coords[center][1]
  del coords[center]
  a,b=getAns(coords,xLine,yLine)
  # print(xLine, yLine)
  print(a,b)
  n=int(input())