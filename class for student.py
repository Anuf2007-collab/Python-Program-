class student:
    def __init__(self,a,b,c):
        self.sno=a
        self.name=b
        self.age=c
    def display(self):
        print("S.no:",self.sno)
        print("Name:",self.name)
        print("Age:", self.age)
x=int(input("Enter no."))
y=input("enter name")
z=int(input("enter age"))
object=student(x,y,z)
object.display()
class result:
    def __init__(self,a,b,c):
        self.m1=a
        self.m2=b
        self.m3=c
        self.total=a+b+c
    def display(self):
        print("m1:",self.m1)
        print("m2:",self.m2)
        print("m3:",self.m3)
        print("total",self.m1+self.m2+self.m3)
        print("avg",self.total/3)
x=int(input("Enter m1:"))
y=int(input("Enter m2:"))
z=int(input("Enter m3:"))
object=result(x,y,z)
object.display()