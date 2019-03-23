N = int(input())
ls = "ABCDEFGH"
for i in range(N):
  temp = input().split(" ")
  x1 = ls.index(temp[0]) + 1
  y1 = int(temp[1])
  x2 = ls.index(temp[2]) + 1
  y2 = int(temp[3])
  nDiff1 = y1 - x1
  nDiff2 = y2 + x2
  nDiff3 = y1 + x1
  nDiff4 = y2 - x2
  diff1 = (nDiff2 - nDiff1) / 2
  diff2 = (nDiff3 - nDiff4) / 2
  sum1 = diff1 + nDiff1
  sum2 = diff2 + nDiff4
  if (diff1 < 1 or diff1 > 8 or sum1 < 1 or sum1 > 8 or diff1 != (diff1)//1):
    sum1 = sum2
    diff1 = diff2
  if (diff1 != (diff1)//1 or diff1 < 1 or diff1 > 8 or sum1 < 1 or sum1 > 8):
    print("Impossible")
  elif (x1 == x2 and y1 == y2):
    print("0 " + temp[0] + " " + temp[1])
  elif (diff1 == x2 and sum1 == y2 or diff1 == x1 and sum1 == y1):
    print("1 " + temp[0] + " " + temp[1] + " " + temp[2] + " " + temp[3])
  else:
    print("2 " + temp[0] + " " + temp[1] + " " + ls[int(diff1) - 1] + " " + str(int(sum1)) + " " + temp[2] + " " + temp[3])