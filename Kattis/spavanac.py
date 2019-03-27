h, m = map(int, input().split())
tot=h*60+m
tot-=45
newH=tot//60
newM=tot%60

if newH<0:
  newH+=24
print(str(newH)+" "+str(newM))