while True:
  n=input()
  c=2
  sum=0
  while sum<float(n):
    sum+=1/c
    c+=1
  if n!="0.00": 
    print(str(c-2)+" card(s)")
  else:
    exit()