def pig_it(text):
    li=text.split()
    for x in range(0, len(li)):
        if li[x] is "." or li[x] is "!" or li[x] is "?":
            li[x]=li[x]
        else:
            li[x]=li[x][1:]+li[x][0]+'ay'
    return " ".join(li)
    