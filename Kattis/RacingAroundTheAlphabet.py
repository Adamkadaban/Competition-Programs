import math
circle = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"

def distance(l1, l2):
  first= (circle.index(l2)-circle.index(l1)) % 28
  second= (circle.index(l1) - circle.index(l2)) % 28
  return min(first, second)

n = int(input())
for i in range(n):
    ins = input().strip()
    total = 0
    curr = ins[0]
    for i in ins[1:]:
        total += distance(curr, i)
        curr = i

    print(((math.pi * 60) / 28 / 15 * total) + len(ins))