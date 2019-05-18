def getNumVowels(word):
  a=word.count("a")
  e=word.count("e")
  i=word.count("i")
  o=word.count("o")
  u=word.count("u")
  return a+e+i+o+u
fin=open("Prob02.in.txt")
T=int(fin.readline())
for i in range(T):
  print(getNumVowels(fin.readline()))
fin.close()