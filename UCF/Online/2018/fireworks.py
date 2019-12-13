file1 = open("fireworks.in")
file2 = open("fireworks.out", "w")

num1 = int(file1.readline().strip())
for i in range(num1):
    num2 = int(file1.readline().strip())
    max = -1
    maxPos = 0
    min = -1
    minPos = 0
    line = file1.readline().strip().split(" ")
    for j in range(num2):
        if min == -1 or int(line[j]) < min:
            min = int(line[j])
            minPos = j + 1
        if max == -1 or int(line[j]) > max:
            max = int(line[j])
            maxPos = j + 1
    file2.write("Scenario #" + str(i + 1) + ":\n")
    file2.write("Highest Firework: " + str(maxPos) + "\n")
    file2.write("Earliest Firework: " + str(minPos) + "\n")
    file2.write("\n")
file1.close()
file2.close()




