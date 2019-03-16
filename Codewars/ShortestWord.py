def find_short(s):
    li=s.split()
    l=len(li[0])
    for i in li:
        if len(i)<l:
            l=len(i)
    return l