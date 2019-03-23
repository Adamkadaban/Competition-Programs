dom={"A":11, "K":4, "Q":3, "J":20, "T":10, "9":14, "8":0, "7":0}

nom={"A":11, "K":4, "Q":3, "J":2, "T":10, "9":0, "8":0, "7":0}

c=0

in1=input().split()
hands=int(in1[0])*4
trump=in1[1]

for i in range(hands):
  temp=input()
  if temp[1]==trump:
    c+=dom.get(temp[0])
  else:
    c+=nom.get(temp[0])
print(str(c))