num = int(input())
count = num
for i in range(2, num):
  for z in range(i**2, num + 1, i):
    count += 1
print(count)