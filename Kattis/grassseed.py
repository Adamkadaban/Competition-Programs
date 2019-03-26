tot=0
c=float(input()) #cost of seeds per m^2
N=int(input()) # number of lines to sow
for i in range(N):
  w, l=map(float, input().split())
  tot+=c*(w*l)
print(str(tot))