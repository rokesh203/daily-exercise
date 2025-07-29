"""def additon():
    a=int(input())
    b=int(input())
    print(a+b)
    
additon()

def findeoro(a):
    if(a%2==0):
        print("even")
    else:
        print("odd")

a=int(input("enter a number:"))
findeoro(a)

def printrange(a,b):
    for i in range(a,b):
        print(i)
        
a=int(input())
b=int(input())
printrange(a,b)

def add(a,b):
    return a+b

a=int(input("enter a number:"))
b=int(input("enter a number"))
c=int(input("enter a number"))

added=add(a,b)

out=added*c

print(out)"""

class Solution(object):
    def checkDivisibility(self, n):
        c=str(n)
        dig1=int(c[0])
        dig2=int(c[1])
        add=dig1+dig2
        prod=dig1*dig2
        total=add+prod
        if(n%total==0):
            print("true")
        else:
            print("false")

s=Solution()
s.checkDivisibility(36)