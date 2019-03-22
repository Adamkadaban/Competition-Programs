n, k, s, =map(int, input().split())
'''
n: number of boxes with screws
k: number of screws needed to make a table
s: number of tables to be made
'''

screws=map(int, input().split())

screws=sorted(screws)[::-1]


tot=k*s

c=0
sum=0
while sum<tot:
  sum+=screws.pop(0) 
  c+=1
print(c)