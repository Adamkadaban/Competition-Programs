import sys
for i in range(int(sys.stdin.readline())):
  sys.stdin.readline()
  inp=sys.stdin.readline().rstrip()
  caps=[i for i in inp if i.isupper()]
  lower=[i for i in inp if i.islower()]
  v="Yes\n" if len(caps)==len(lower) else "No\n"
  sys.stdout.write("Sentence #"+str(i+1)+": "+v)