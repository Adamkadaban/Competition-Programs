def get_sum(a,b):
    if a==b:
        return a
    x=0
    for i in list(range(min(a,b),max(a,b)+1)):
        x+=i
    return x


#Alt solution
'''
def get_sum(a,b):
    if a==b:
        return a
    else:
        return sum(list(range(min(a,b), max(a,b)+1)))
'''