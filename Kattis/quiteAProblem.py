import sys
for i in sys.stdin.readlines():
  i=i.rstrip()
  i=i.lower()
  if "problem" in i:
    print("yes")
  else:
    print("no")