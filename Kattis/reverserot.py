s="ABCDEFGHIJKLMNOPQRSTUVWXYZ_.ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

# in1=input().split()
# n=int(in1[0])
# l=in1[1]
def getAns(n, l):
  l=l[::-1]
  new=[s[s.find(x)+n] for x in l]
  print("".join(new))
con=True
while con:
  x=input().split()
  if x==["0"]:
    con=False
  elif len(x)==2:
    getAns(int(x[0]), x[1])