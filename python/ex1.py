a=[]
print("enter 4 number")
for i in range(4):
    num = int(input("enter number:"+str(i+1) +":"))
    a.append(num)
    
print(a)

sum=0
for i in a:
    sum =sum+i
    print(sum)



sum = 0
for i in range(1,):
    sum += i
    print(sum)
    
    
for i in range(5):
    print(str(i)+"cube of the "+str(i+1)+"is :"+str(i*i*i))
    
for i in range(1,10):
    for j in range(1,6):
        print(j,"apple")
        

for i in range(1,3):
    print("week :",i)
    for j in range(1,4):
        print("day :",j)


for i in range(1,5):
    print()
    for j in range(1,i+1):
        print("*",end="")
i=1
while(i<6):
    print(i)
    i=i+1
    
i=10
while(i<210):
    print(i,end="")
    i=i+10
    
i=10
while(i>0):
    print(i,end=",")
    i=i-1
    
i=5
fact=1
while(i>0):
    fact =fact*i
    i=i-1
    print(fact)
    