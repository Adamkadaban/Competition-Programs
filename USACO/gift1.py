"""
ID: adamkad1
LANG: PYTHON3
TASK: gift1
"""
from collections import OrderedDict as od

f1 = open ('gift1.in')
f2 = open ('gift1.out', 'w')
li = od()

n = int(f1.readline())

for x in range(0, n):
    li[f1.readline().strip()] = 0
for x in range(0, n):
    name = f1.readline().strip()
    gift = map(int, f1.readline().split())
    numOfGifts=map(int, f1.readline().split())
    for j in range(0, numOfGifts):
        done = f1.readline().strip()
        li[done] += gift / numOfGifts
        li[name] -= gift / numOfGifts

for x in li:
    f2.write(x + " " + str(li[x]) + "\n")

f1.close()
f2.close()