from collections import Counter
cards=input().split(" ")
for x in range(0, len(cards)):
    cards[x]=cards[x][0:1]
most = Counter(cards).most_common(1)[0]
print(most[1])