fin=open("Prob01.in.txt")
for i in fin:
  if int(i.strip())<70:
    print("FAIL")
  else:
    print("PASS")
fin.close()