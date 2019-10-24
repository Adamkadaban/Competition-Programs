import string
alph=string.ascii_lowercase
ins=input()
table = [[0 for i in range(len(ins) + 1)] for j in range(len(alph) + 1)]
for i in range(1, len(alph)+1):
  for j in range(1, len(ins)+1):
    if alph[i-1] == ins[j-1]:
      table[i][j] = 1 + table[i-1][j-1]
    else:
      table[i][j] = max(table[i-1][j], table[i][j-1])
r=26-table[-1][-1]
print(r)