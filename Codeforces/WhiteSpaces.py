def number(num):
  if num==3 :
    return 0
  return number(num-(num//4))+ 1
print(number(int(input()) * 3))