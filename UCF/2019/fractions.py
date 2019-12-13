import sys
def getAns(arr):
  for i in arr:
    for j in arr:
      if i!=j and j>i:
        if j%i!=0:
          return False
  return True
for i in range(int(sys.stdin.readline())):
  sys.stdin.readline()
  vals=list(map(int, sys.stdin.readline().split()))
  val="This array is bae!\n" if getAns(vals) else "Go away!\n"
  sys.stdout.write("Array #"+str(i+1)+": "+val)