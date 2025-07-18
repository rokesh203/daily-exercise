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




"""sum = 0
for i in range(1,):
    sum += i
    print(sum)
    """