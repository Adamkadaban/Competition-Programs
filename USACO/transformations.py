"""
ID: adamkad1
PROG: transform
LANG: PYTHON3
"""
def rot90(arr):
    return list(zip(*arr[::-1]))

def rot180(arr):
    return rot90(rot90(arr))

def rot270(arr):
    return rot180(rot90(arr))

def flip(arr):
    return arr[::-1]


def comb(arr):
    a = flip(arr)
    b = rot90(a)
    c = rot180(a)
    d = rot270(a)
    if equals(b, result) or equals(c, result) or equals(d, result):
        return True
    return False


def equals(arr, result):
    return (arr) == (result)


f = open("transform.in")
f = open("transform.out", "w")
N = int(f.readline().strip())
arr = [[x for x in range(N)] for i in range(N)]
result = [[x for x in range(N)] for i in range(N)]
for x in range(N):
    arr[x] = list(f.readline().strip("\n"))
for x in range(N):
    result[x] = list(f.readline().strip("\n"))
s = 7
if equals(rot90(arr), result):
    s = 1
elif equals(rot180(arr), result):
    s = 2
elif equals(rot270(arr), result):
    s = 3
elif equals(flip(arr), result):
    s = 4
elif comb(arr):
    s = 5
elif equals(arr, result):
    s = 6

f.close()
f.write(str(s) + "\n")
f.close()