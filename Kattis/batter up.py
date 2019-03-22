input()
ins=map(int, input().split())
ins=[x for x in ins if x != -1]
print(sum(ins)/len(ins))