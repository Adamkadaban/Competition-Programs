def spin_words(sentence):
    new=sentence.split(" ")
    r=[]
    for x in range(0, len(new)):
        if len(new[x]) >=5:
            r.append(new[x][::-1])
        else:
            r.append(new[x])
    return " ".join(r)