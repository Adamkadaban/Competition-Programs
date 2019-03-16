temp = input().split(" ")
piles = int(temp[0])
turns = int(temp[1])
pilesList = []

for i in range(piles):
    pilesList.append(int(input()))

tot = 0
for i in range(turns):
    maximum = 0
    index = -1
    for j in range(piles):
        if(maximum < pilesList[j]):
            maximum = pilesList[j]
            index = j
    pilesList[index] = pilesList[index] - pilesList[index] // 2
    tot = tot + maximum // 2
print(tot)