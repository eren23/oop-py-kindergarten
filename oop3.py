
#inherits extends override 
class Employee():
    def __init__(self, name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary
    def work(self):
        print(f"{self.name}, working")

class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name,age,salary)
        self.level=level

    def debug(self):
        print(f"{self.name}, debuggin'")

    def work(self):
        print(f"{self.name}, coding")
        
        

class Designer(Employee):
    
    def draw(self):
        print(f"{self.name}, draw")

    def work(self):
        print(f"{self.name}, creating")
        

se = SoftwareEngineer("Eren", 24, 5000,"Junior")
#  

d = Designer("Ece", 21, 6000)
# print(d.name, d.age)
# d.work()
# d.draw()

#Polymorphism

employees = [SoftwareEngineer("Bico", 24, 6999,"Senior"),
             SoftwareEngineer("Erdu", 28, 3999,"Junior"),
             Designer("Elif", 22, 6000)]
 
def motive_employees(employees):
    for e in employees:
        e.work()

motive_employees(employees)

#Recap:
#inheritance Child(Base):
#inherit, extends, override
#super().__init__
#polymorphism