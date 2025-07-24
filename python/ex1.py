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




def validate(uname,upass):
    s_uname="rokesh"
    s_pass="123"
    if uname==s_uname and upass==s_pass:
        print("True")
    else:
        print("false")
    
    
a=input("enter the name")
b=input("enter the password")
validate(a,b)



class vinoth:
    drink=""
    def read(self):
        print("aptitude")
    
    def phone(self):
        print("reels")
        

rokesh =vinoth()
gowri = vinoth()

rokesh.phone()


class goa:
    name=""
    drink=""
    def party(self):
        print("lets party")
    def beach(self):
      print("lets swim")
      
ramesh=goa()
suresh=goa()

ramesh.name="ramesh"
suresh.drink="beer"

ramesh.drink="yes"
suresh.drink="No"

print("Ramesh drink")
print("drink :",ramesh.drink)
print("Suresh Drink")
print("drink :",suresh.drink)

class laptop:
    price=""
    processor=""
    Ram=""
    def lap1():
        print("HP laptop")
    def lap2():
        print("dell laptop")
    def lap3():
        print("lenovo laptop")
        
HP=laptop()
Dell=laptop()
Len=laptop()

HP.price="50000"
HP.processor="i5"
HP.Ram="32Gb"
print("HP"+HP.price,HP.processor,HP.Ram)

Dell.price="60000"
Dell.processor="i6"
Dell.Ram="32Gb"
print("Dell"+Dell.price,Dell.processor,Dell.Ram)


Len.price="50000"
Len.processor="i5"
Len.Ram="32Gb"
print("Lenovo"+Len.price,Len.processor,Len.Ram)