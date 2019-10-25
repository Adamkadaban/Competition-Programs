s=list(input())
l=len(s)
tot=2**l
minx=0
maxx=tot-1
miny=0
maxy=tot-1
for i in range(l):
  if s[i]=='0':
    maxx=(maxx+minx)//2
    maxy=(maxy+miny)//2
  if s[i]=='1':
    minx=((maxx+minx)//2)
    maxy=(maxy+miny)//2
  if s[i]=='2':
    maxx=(maxx+minx)//2
    miny=((maxy+miny)//2)
  if s[i]=='3':
    minx=((maxx+minx)//2)
    miny=((maxy+miny)//2)
  
print(l,maxx,maxy)