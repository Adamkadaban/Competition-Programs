"""
ID: adamkad1
PROG: palsquare
LANG: PYTHON3
"""

def changeBase(n,b):
   nums = "0123456789ABCDEFGHIJ"
   if n < b:
      return nums[n]
   else:
      return changeBase(n//b,b) + nums[n%b]

def isPalindrome(num):
  if str(num) == str(num)[::-1]:
    return True

f = open("palsquare.in")
b = int(f.readline().rstrip())
f.close
f = open("palsquare.out","w")
nums=[str(x) for x in range(1,301) if isPalindrome(changeBase(x**2, b))]

for x in range(len(nums)):
  f.write(changeBase(int(nums[x]), b)+" "+ str(changeBase(int(nums[x])**2,b))+"\n")
f.close()