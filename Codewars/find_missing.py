def find_missing(sequence):
    l=len(sequence)+1
    i=(sequence[0]+sequence[-1])//l
    corr=list(range(sequence[0], sequence[-1]+1, i))
    for i in corr:
        if i not in sequence:
            return i