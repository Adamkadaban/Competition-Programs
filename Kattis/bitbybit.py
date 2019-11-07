def AND(a, b):
  # print(a, b)
  if a=="0" or b=="0":
    return "0"
  if a=="?" or b=="?":
    return "?"
  else:
    return str(int(a)&int(b))
  
def OR(a, b):
  if a=="0" and b=="0":
    return "0"
  if a=="1" or b=="1":
    return "1"
  else:
    return "?"
  
def getAns(ins):
  num=["?"]*32
  for i in ins:
    inst=i[0]
    v=int(i[1])
    if inst=="CLEAR":
      num[31-v]="0"
    if inst=="SET":
      num[31-v]="1"
    if inst=="OR":
      first=num[31-v]
      second=num[31-int(i[2])]
      num[31-v]=OR(first, second)
    if inst=="AND":
      first=num[31-v]
      second=num[31-int(i[2])]
      num[31-v]=AND(first, second)
    # print(num)
  return "".join(num)

def toNum(x):
  for i in range(len(x)):
    if len(x[i])==1:
      x[i]=int(x[i])
  return x

n=int(input())
while n!=0:
  instructions=[]
  for _ in range(n):
    v=input().split()
    instructions.append(v) 
  print(getAns(instructions))
  n=int(input())
