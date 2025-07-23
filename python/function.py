def additon():
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

print(out)
