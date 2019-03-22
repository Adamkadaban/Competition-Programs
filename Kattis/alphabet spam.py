ins=list(input())
tot=len(ins)
whitespace=[x for x in ins if x=="_"]
lower=[x for x in ins if x.isalpha() and x.lower()==x]
upper=[x for x in ins if x.isalpha() and x.upper()==x]
w=len(whitespace)
l=len(lower)
u=len(upper)

s=tot-w-l-u
print(str(w/tot))
print(str(l/tot))
print(str(u/tot))
print(str(s/tot))