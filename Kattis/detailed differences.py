N=int(input())
for i in range(N):
  a=list(input())
  b=list(input())
  r=""
  for i in range(len(a)):
    if a[i]==b[i]:
      r+="."
    else:
      r+="*"
  print("".join(a))
  print("".join(b))
  print(r+"\n")