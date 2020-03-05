import sys
from math import pi
N=int(sys.stdin.readline())
for i in range(N):
  r, n = map(int, sys.stdin.readline().split())
  oArea=pi*(r**2)
  numC=4
  tot=oArea

  adder=oArea*numC/4

  for i in range(0, n-1):
    tot+=adder
    adder*=.75
  sys.stdout.write(str(tot)+"\n")