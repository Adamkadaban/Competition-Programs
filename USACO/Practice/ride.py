"""
ID: adamkad1
LANG: PYTHON3
TASK: ride
"""
fin = open('ride.in')
fout = open('ride.out','w')
prod = 1
for x in fin.readline()[:-1]:
    prod *= ord(x)-64
prod1 = 1
for x in fin.readline()[:-1]:
    prod1 *= ord(x)-64
if prod%47==prod1%47:
    s = "GO\n"
else:
    s = "STAY\n"
fout.write(s)
fout.close