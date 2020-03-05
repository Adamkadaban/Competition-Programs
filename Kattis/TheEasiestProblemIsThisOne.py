n = int(input())
def sum_digits(number):
  t = 0
  for i in str(number):
    t += int(i)
  return t

while n != 0:
  a = True
  i = 11
  while a:
    if sum_digits(n) == sum_digits(i*n):
      a = False
      print(i)
    i += 1
  n = int(input()) 