#find the sign of the product of all numbers between 2 inputs
# a<=b
'''
input:
	a b
output:
	if product of numbers from a to b inclusive is:
		negative:
			-1
		0:
			0
		positive:
			1




#i didnt know how to do this at first bc the numbers were to large buttt...


a,b=map(int, input().split())
if a<=0 and b>=0:
  print(0)
if b<=0 and a>=0:
  print(0)
if b>0 and a>0:
  print(1)
if a<0 and b<0:
  if abs(a-b)%2==0:
    print(-1)
  else:
    print(1)