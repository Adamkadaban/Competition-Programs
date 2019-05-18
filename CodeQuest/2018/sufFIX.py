# def test(a):
#   if a[-1]=="1":
#     b="st"
#   if a[-1]=="2":
#     b="nd"
#   if a[-1]=="3":
#     b="rd"
#   if a[-1]=="4" or a[-1]=="0" or a[-1]=="5" or a[-1]=="6" or a[-1]=="7" or a[-1]=="8" or a[-1]=="9" or int(a)==12 or int(a)==13:
#     b="th"
#   return a+b
def getSuffixed(a):
  a=a[:-3]
  # print("lol",a)
  if a[-1]=="1":
    b="st"
  if a[-1]=="2":
    b="nd"
  if a[-1]=="3":
    b="rd"
  if a[-1]=="4" or a[-1]=="0" or int(a)==12:
    b="th"
  return a+b
fin=open("Prob03.in.txt")
N=int(fin.readline())
for i in range(N):
  print(getSuffixed(fin.readline()))
# for i in range(111): # testing
#   print(test(str(i)))
fin.close()