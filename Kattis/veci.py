from itertools import permutations
n=input()
perms=[int(''.join(p)) for p in permutations(n)]
perms=[i for i in perms if i>int(n)]
if len(perms)==0:
  print("0")
else:
  print(min(perms))