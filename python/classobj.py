"""class vinoth:
    drink=""
    def read(self):
        print("aptitude")
    
    def phone(self):
        print("reels")
        

rokesh =vinoth()
gowri = vinoth()

rokesh.phone()
gowri.read()

class student:
    def __init__(self):
        name=""
        register=""
    def display(self):
        print("name",self.name)
        print("register",self.register)
        
stu = student()
stu.name="rokesh"
stu.register=123
stu.display()

class Fruit:
    def __init__(self,col):
        self.color=col
        
apple=Fruit("red")
print(apple.color)"""

class Teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print("name :",self.name)
        print("regno :",self.regno)
        
t1=Teacher("rokesh","123")
t2=Teacher("raj","124")
        
t1.display()
t2.display()

