N=int(input())
for __ in range(N):
  n, b = map(int, input().split())
  
  board=[0]*2000
  j=0
  for _ in range(b):
    for i in range(1, len(board)+1):
      j=max(i,j)
      if board[i]==0:
        board[i]=i
        break
      else:
        board[i]=board[i]-1


  outp=[]
  for i in range(1,j+1):
    outp.append(board[i])
    if i%10==0 and i!=j:
      outp.append("spl")
  # print(outp)
  print(n, outp[-1])
  for i in outp:
    if i=="spl":
      print()
    else:
      print(i, end=" ")
    
