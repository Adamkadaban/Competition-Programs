def getAns(lis):
  p=1
  for i in lis.items():
    x=i[1].split()
    # print(x)
    p=p*(len(x)+1)
  return p-1

N=int(input())
for i in range(N):
  T=int(input())
  ins={}
  for i in range(T):
    
    a, b = map(str, input().split())
    if b not in ins:
      ins[b]=a
    else:
      temp=ins[b]
      ins[b]=a+" "+temp
  # print(ins)
  print(getAns(ins))    
  # print(ins)

    
# x={'headgear': 'turban hat', 'eyewear': 'sunglasses'}

# 
