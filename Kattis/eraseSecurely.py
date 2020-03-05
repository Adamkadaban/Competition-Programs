n = int(input())

diff = [a==b for a,b in zip(input(), input())]

if (n%2!=0 and sum(diff)==0) or (n%2==0 and all(diff)):
    print('Deletion succeeded')
else:
    print('Deletion failed')