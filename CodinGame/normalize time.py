'''
Given a first line of N test cases, normalize the times given in each case


Input:
	4
	10:20:02
	12:35:62
	02:66:02
	00:0000:00

Output:
	10:20:02
	12:36:02
	03:06:02
	00:00:00
'''

#Code:

for i in range(int(input())):
    t=list(map(int,input().split(":")))
    t[1]+=t[2]//60
    t[2]=t[2]%60
    t[0]+=t[1]//60
    t[1]=t[1]%60
    print(":".join(map(lambda x:str(x).zfill(2),t)))

        