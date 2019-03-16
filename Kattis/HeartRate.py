num = int(input())
for i in range(num):
    temp = input().split(" ")
    b = int(temp[0])
    p = float(temp[1])
    BPM = (60 * b) / p
    deviation = 60 / p
    print(str(round(BPM - deviation, 4)) + " " + str(round(BPM, 4)) + " " + str(round(BPM + deviation, 4)))
