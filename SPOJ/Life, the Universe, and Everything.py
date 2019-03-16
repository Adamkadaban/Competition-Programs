ins=[]
ins.append(int(input()))
while ins[-1] != 42:
  ins.append(int(input()))
for x in ins[:-1]:
	print(str(x))