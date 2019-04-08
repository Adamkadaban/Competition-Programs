def rot(s, n):
  r=s
  nr=""
  for i in range(len(r)):
    currVal=(ord(r[i])-65+n)%26
    nr+=chr(currVal+65)
  return nr

def getVal(s):
  r=0
  for i in s:
    r+=ord(i)-65
  return r

s=input()
l=len(s)
s1=s[:l//2]
s2=s[l//2:] # splits

n1=getVal(s1)
n2=getVal(s2)

ns1=rot(s1, n1)
ns2=rot(s2, n2) #works up to here


r=""
for i in range(len(ns1)):
  val=ord(ns1[i])-65
  val2=ord(ns2[i])-65
  outs=chr((val+val2)%26+65)
  r+=outs
print(r)