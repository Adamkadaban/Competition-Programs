def iq_test(numbers):
    numE=0
    numO=0
    cl=numbers.split()
    for x in cl:
        if int(x)%2==0:
            numE+=1
        else:
            numO+=1
    if numE>numO:
        for x in cl:
            if int(x)%2==1:
                return cl.index(x)+1
    else:
        for x in cl:
            if int(x)%2==0:
                return cl.index(x)+1