num1=["    +  +---+     +   +  +---+",
      "    |  |         |   |      |",
      "    |  |      o  |   |      |",
      "    +  +---+     +---+      +",
      "    |  |   |  o      |      |",
      "    |  |   |         |      |",
      "    +  +---+         +      +"]


num2=["+---+  +---+     +---+  +---+",
      "    |      |     |      |   |",
      "    |      |  o  |      |   |",
      "+---+  +---+     +---+  +---+",
      "|          |  o      |      |",
      "|          |         |      |",
      "+---+  +---+     +---+  +---+"]

num3=["+---+  +---+     +---+  +---+",
      "|   |  |   |     |   |  |   |",
      "|   |  |   |  o  |   |  |   |",
      "+   +  +   +     +   +  +---+",
      "|   |  |   |  o  |   |  |   |",
      "|   |  |   |     |   |  |   |",
      "+---+  +---+     +---+  +---+"]
zero=[i[:5] for i in num3]
one=[i[:5] for i in num1]
two=[i[:5] for i in num2]
three=[i[7:12] for i in num2]
four=[i[17:22] for i in num1]
five=[i[17:22] for i in num2]
six=[i[7:12] for i in num1]
seven=[i[24:29] for i in num1]
eight=[i[24:29] for i in num3]
nine=[i[24:29] for i in num2]
colon=[i[14] for i in num1]



dic={"0":zero, "1":one, "2":two, "3":three, "4":four, "5":five, "6":six, "7":seven, "8":eight, "9":nine,":":colon}
x=input()
while x!="end":
  arr=[]
  nums=list(x)
  for i in range(len(nums)):
    arr.append(dic[nums[i]])
    if i!=len(nums)-1:
      arr.append("       ")
      arr.append("       ")

  
  for j in range(len(arr[0])):
    for i in range(len(arr)):
      print(arr[i][j],end="")
    print()
  print()
  print()
  x=input()
print("end")