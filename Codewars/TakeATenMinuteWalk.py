def isValidWalk(walk):
    x=0
    if len(walk)!=10:
        return False
    for i in walk:
        if i=='n':
            x+=1
        if i=='s':
            x+=-1
        if i=='e':
            x+=2
        if i=='w':
            x+=-2
    if x==0:
        return True
    else:
        return False