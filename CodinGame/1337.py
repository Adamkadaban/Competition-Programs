# convert a string input into 1337 code
# input "Hello World" >> Output "H3110 W0r1d" 

s=list(input())

x={"o":0, "l":1, "z":2, "e":3, "a":4, "s":5, "g":6, "t":7, "b":8, "q":9}
for i in range(len(s)):
    if s[i].lower() in x.keys():
        s[i]=x.get(s[i].lower())

s=list(map(str, s))
        
print("".join(s))