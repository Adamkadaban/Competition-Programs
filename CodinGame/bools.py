'''
inputs:
	m: logical operator
	a: 0 or 1 (binary boolean var 1)
	b: 0 or 1 (binary boolean var 2)
	r: 0 or 1 (binary boolean result)
output:
	true or false (lower case)

'''
#output if the statement is true [ie. print(a m b == r)]


m = input()
a = int(input())
b = int(input())
r=int(input())

y=bool(a)
z=bool(b)
n=bool(r)

x=1
if m=="AND":
    x=(a*b==r)
elif m=="OR":
    x=y or z==n
else:
    x=(y!=z) and y or z == n
print(str(x).lower())