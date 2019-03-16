x=int(input())
n=int(input())
li=[]
c=0
while c<n:
    li.append(int(input()))
    c+=1
print(str(x+(x*n)+(-1*sum(li))))