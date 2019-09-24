n=int(input())
nums=list(map(int, input().split()))
evs=len([i for i in nums if i%2==0])
print(min(n-evs, evs))