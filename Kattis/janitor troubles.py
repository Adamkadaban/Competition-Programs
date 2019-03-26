a, b, c, d=map(int, input().split())
s=(a+b+c+d)/2
x=((s-a)*(s-b)*(s-c)*(s-d))**.5
print(str(x) if int(x)!= x else str(int(x))) # so i realized this want necessary afterwards but whatever it works