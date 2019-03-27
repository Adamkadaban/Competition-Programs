n, w, h=map(int, input().split())
for i in range(n):
  x=int(input())
  print("DA" if x <= (h**2+w**2)**.5 else "NE")